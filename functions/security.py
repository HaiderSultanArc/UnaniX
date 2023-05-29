from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

import utils.secrets as secrets

passwordContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verifyPassword(plainPassword, hashedPassword):
    """
    Verify Password
    ===============
    Parameters:
    -----------
        plainPassword:
            description: Plain password
            dtype: str
        hashedPassword:
            description: Hashed password
            dtype: str
    -----------
    Returns:
    --------
        verified:
            description: Whether the password is verified or not
    """
    return passwordContext.verify(plainPassword, hashedPassword)


def getHashedPassword(password):
    """
    Get Hashed Password
    ===================
    Parameters:
    -----------
        password:
            description: Plain password
            dtype: str
    -----------
    Returns:
    --------
        hashedPassword:
            description: Hashed password
            dtype: str
    """
    return passwordContext.hash(password)


def createAccessToken(data: dict, expiresDelta: timedelta | None = None):
    """
    Create Access Token
    ===================
    Parameters:
    -----------
        data:
            description: Data to be encoded in the token
            dtype: dict
        expiresDelta:
            description: Time after which the token expires
            dtype: timedelta
    -----------
    Returns:
    --------
        token:
            description: Access Token
            dtype: str
    """
    toEncode = data.copy()
    
    if expiresDelta:
        expire = datetime.utcnow() + expiresDelta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    toEncode.update({"exp": expire})
    encodedJWT = jwt.encode(toEncode, key=secrets.SECRET_KEY, algorithm=secrets.ALGORITHM)
    
    return encodedJWT