from datetime import timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

import backend.schemas as sc
import functions.database as db
import functions.security as sec
import utils.secrets as secrets

# ***-***-***-***-***-***-***-***-*** AUTHENTICATION ***-***-***-***-***-***-***-***-*** #
OAuth2Schema = OAuth2PasswordBearer(tokenUrl="token")


def authenticateUser(email: str, password: str) -> sc.User:
    """
    Authenticate user with email and password
    =========================================
    Parameters:
    -----------
        email:
            description: Email of the user
            dtype: str
        password:
            description: Password of the user
            dtype: str
    -----------
    Returns:
    --------
        user:
            description: User object
            dtype: schemas.User
    """
    userResponse = db.getUserByEmail(email)

    if userResponse["success"]:
        user = userResponse["data"]
        
        if not sec.verifyPassword(password, user.hashedPassword):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect Password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        else:
            return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=userResponse["message"],
            headers={"WWW-Authenticate": "Bearer"},
        )


def loginForAccessToken(email: str, password: str) -> dict:
    """
    Login for access token
    ======================
    Parameters:
    -----------
        email:
            description: Email of the user
            dtype: str
        password:
            description: Password of the user
            dtype: str
    -----------
    Returns:
    --------
        dict:
            description: Dictionary containing access token
    """
    authUser = authenticateUser(email, password)
        
    accessTokenExpires = timedelta(minutes=secrets.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    accessToken = sec.createAccessToken(
        data={"sub": authUser.email},
        expiresDelta=accessTokenExpires
    )
    
    return {
        "access_token": accessToken,
        "token_type": "bearer"
    }


def getCurrentUser(token: str = Depends(OAuth2Schema)) -> sc.User:
    """
    Get Current User
    ================
    Parameters:
    -----------
        token:
            description: Access token
            dtype: str
    -----------
    Returns:
    --------
        user:
            description: User object
            dtype: schemas.User
    """
    try:
        payload = jwt.decode(token, secrets.SECRET_KEY, algorithms=[secrets.ALGORITHM]) # type: ignore
        email = payload.get("sub")
        
        if email is None:
            raise JWTError("Invalid Token")
        
        tokenData = sc.TokenData(email=email)
    except JWTError as error:
        raise HTTPException(status_code=401, detail=str(error))
    
    userResponse = db.getUserByEmail(email=tokenData.email)

    if userResponse["success"]:
        return userResponse["data"]
    else:
        raise HTTPException(status_code=401, detail=userResponse["message"])


def getCurrentActiveUser(currentUser: sc.User = Depends(getCurrentUser)) -> sc.User:
    """
    Get Current Active User
    =======================
    Parameters:
    -----------
        currentUser:
            description: Current user object
            dtype: schemas.User
    -----------
    Returns:
    --------
        user:
            description: User object
            dtype: schemas.User
    """
    if currentUser.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    return currentUser