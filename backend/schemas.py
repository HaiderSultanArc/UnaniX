from pydantic import BaseModel


class User(BaseModel):
    firstName              : str
    lastName               : str
    email                  : str
    password               : str
    gender                 : str | None = None
    phone                  : str | None = None
    age                    : int | None = None
    dob                    : str | None = None
    avatar                 : str | None = None
    address                : str | None = None
    disabled               : bool | None = False


class Patient(User):
    patientID              : str
    diseases               : list | None = None
    symptoms               : list | None = None
    appointments           : list | None = None
    practitioners          : list | None = None


class Practitioner(User):
    practitionerID         : str
    patients               : list | None = None
    appoinments            : list | None = None
    specialization         : str | None = None


class Disease(BaseModel):
    name_eng               : str | None = None
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    icd_code               : str | None = None
    description            : str | None = None


class Symptom(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class Cause(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class TreatmentPrinciple(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class Drug(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class RegimentalTherapy(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class PharmacoTherapy(BaseModel):
    name_eng               : str | None = None
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str


class Diet(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class Prevention(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


# --------------------------------- #

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str