import database.database as db
import database.schemas as sc
import utils.auth as auth
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm

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



# ***-***-***-***-***-***-***-***-*** GET ***-***-***-***-***-***-***-***-*** #

@app.post('/get_patient_by_email')
async def get_patient(patientQuery: sc.PatientQuery, authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
    return db.getPatientByEmail(patientQuery.email, session) # type: ignore


@app.post('/get_practitioner_by_email')
async def get_practitioner(practitionerQuery: sc.PractitionerQuery, authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
    return db.getPractitionerByEmail(practitionerQuery.email, session) # type: ignore


# ***-***-***-***-***-***-***-***-*** ADD ***-***-***-***-***-***-***-***-*** #

@app.post('/add_practitioner')
async def add_practitioner(practitioner: sc.User, session: Session = Depends(db.getSession)):
    return db.addPractitioner(practitioner, session)


@app.post('/add_patient')
async def add_patient(patient: sc.User, session: Session = Depends(db.getSession)):
    print(patient)
    return db.addPatient(patient, session)


# @app.post('/add_disease')
# async def add_disease(disease: sc.Disease, authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
#     return db.addDisease(disease, session)


# @app.post('/add_symptom')
# async def add_symptom(symptom: sc.Symptom, authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
#     return db.addSymptom(symptom, session)
    
    
# @app.post('/add_appointment')
# async def add_appointment(appointment: sc.Appointment, authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
#     return db.addAppointment(appointment, session)
    

# @app.post('/add_patient_appointment')
# async def add_patient_appointment(patientAppointment: sc.NewPatientAppointment, authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
#     return db.addPatientAppointment(patientAppointment, session)
    



# ***-***-***-***-***-***-***-***-*** ASSIGN ***-***-***-***-***-***-***-***-*** #

@app.post('/assign_patient_to_practitioner')
async def assign_patient_to_practitioner(patientID: str, practitionerID: str, authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
    return db.assignPatientToPractitioner(patientID, practitionerID, session)


@app.post('/assign_practitioner_to_patient')
async def assign_practitioner_to_patient(pracitionerID: str, patientID: str, authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
    return db.assignPractitionerToPateint(pracitionerID, patientID, session)




# ***-***-***-***-***-***-***-***-*** RETRIEVE ***-***-***-***-***-***-***-***-*** #

@app.post('/retrieve_all_practitioners')
async def retrieve_all_practitioners(authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
    return db.getAllPractitioners(session)


@app.post('/retrieve_all_patients')
async def retrieve_all_patients(authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
    return db.getAllPatients(session)


@app.post('/get_practitioners_by_patient')
async def get_practitioners_by_patient(patientQuery: sc.PatientQuery, authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
    return db.getPractitionersByPatient(patientQuery.patientID, session) # type: ignore


@app.post('/get_patients_by_practitioner')
async def get_patients_by_practitioner(practitionerQuery: sc.PractitionerQuery, authUser: sc.User = Depends(auth.getCurrentActiveUser), session: Session = Depends(db.getSession)):
    return db.getPatientsByPractitioner(practitionerQuery.practitionerID, session) # type: ignore

# ***-***-***-***-***-***-***-***-*** Sign In ***-***-***-***-***-***-***-***-*** #

# @app.post("/token", response_model=sc.Token)
# async def login_for_access_token(credentials: OAuth2PasswordRequestForm = Depends()):
#     return auth.loginForAccessToken(credentials.username, credentials.password)
    

@app.post("/token", response_model=sc.Token)
async def login_for_access_token(credentials: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(db.getSession)):
    return auth.loginForAccessToken(credentials.username, credentials.password, session)