from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm

import backend.schemas as sc
import functions.auth as auth
import functions.database as db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# ***-***-***-***-***-***-***-***-*** AUTHENTICATION ***-***-***-***-***-***-***-***-*** #

# @app.post('/patient_login')
# async def patient_login(data: sc.IDToken):
#     return db.patientLogin(data.IDToken)
    

# @app.post('/practitioner_login')
# async def practitioner_login(data: sc.IDToken):
#     return db.practitionerLogin(data.IDToken)


# @app.post('/patient_login')
# async def patient_login(patientCredentials: sc.PatientLogin):
#     return db.patientLogin(patientCredentials)



@app.post('/get_patient_by_email')
async def get_patient(email: str, authUser: sc.User = Depends(auth.getCurrentActiveUser)):
    return db.getPatientByEmail(email)


@app.post('/get_practitioner_by_email')
async def get_practitioner(email: str, authUser: sc.User = Depends(auth.getCurrentActiveUser)):
    return db.getPractitionerByEmail(email)


@app.post('/add_practitioner')
async def add_practitioner(practitioner: sc.User):
    return db.addPractitioner(practitioner)


@app.post('/add_patient')
async def add_patient(patient: sc.User):
    return db.addPatient(patient)


# @app.post('/add_disease')
# async def add_disease(disease: sc.Disease, authUser: sc.User = Depends(auth.getCurrentActiveUser)):
#     return db.addDisease(disease)


# @app.post('/add_symptom')
# async def add_symptom(symptom: sc.Symptom, authUser: sc.User = Depends(auth.getCurrentActiveUser)):
#     return db.addSymptom(symptom)
    
    
# @app.post('/add_appointment')
# async def add_appointment(appointment: sc.Appointment, authUser: sc.User = Depends(auth.getCurrentActiveUser)):
#     return db.addAppointment(appointment)
    

# @app.post('/add_patient_appointment')
# async def add_patient_appointment(patientAppointment: sc.NewPatientAppointment, authUser: sc.User = Depends(auth.getCurrentActiveUser)):
#     return db.addPatientAppointment(patientAppointment)
    




@app.post('/assign_patient_to_practitioner')
async def assign_patient_to_practitioner(patientID: str, practitionerID: str, authUser: sc.User = Depends(auth.getCurrentActiveUser)):
    return db.assignPatientToPractitioner(patientID, practitionerID)


@app.post('/retrieve_all_practitioners')
async def retrieve_all_practitioners(authUser: sc.User = Depends(auth.getCurrentActiveUser)):
    return db.getAllPractitioners()


@app.post('/retrieve_all_patients')
async def retrieve_all_patients(authUser: sc.User = Depends(auth.getCurrentActiveUser)):
    return db.getAllPatients()


@app.post('/get_practitioners_by_patient')
async def get_practitioners_by_patient(email: str, authUser: sc.User = Depends(auth.getCurrentActiveUser)):
    return db.getPractitionersByPatient(email)


@app.post('/get_patients_by_practitioner')
async def get_patients_by_practitioner(email: str, authUser: sc.User = Depends(auth.getCurrentActiveUser)):
    return db.getPatientsByPractitioner(email)


@app.post("/token", response_model=sc.Token)
async def login_for_access_token(credentials: OAuth2PasswordRequestForm = Depends()):
    return auth.loginForAccessToken(credentials.username, credentials.password)