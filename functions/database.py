import os
from ctypes import addressof
from hmac import new

import django

import functions.security as security

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")
django.setup()

import uuid

import backend.models as models
import backend.schemas as schemas


def getUserByEmail(email: str):
    """
    Get User by Email
    =================
    Parameters:
    -----------
        email:
            description: User Email
            dtype: str
    -----------
    Returns:
    --------
        description: Success or Error Message
        dtype: dict
        Response Model: {
            "success": True or False,
            "message": Response Text,
            "data": object | None
        }
    """
    
    try:
        user = models.User.objects.get(email=email)
        
        return {
            "success": True,
            "message": "User Found",
            "data": user
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Error while getting user with email: {email}. {error}",
            "data": None
        }


def getPractionerByEmail(email: str):
    """
    Get Practioner by Email
    =======================
    Parameters:
    -----------
        email:
            description: Practioner Email
            dtype: str
    -----------
    Returns:
    --------
        description: Success or Error Message
        dtype: dict
        Response Model: {
            "success": True or False,
            "message": Response Text,
            "data": object | None
        }
    """
    
    try:
        practioner = models.Practitioner.objects.get(email=email)
        
        return {
            "success": True,
            "message": "Practioner Found",
            "data": practioner
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Error while getting practioner with email: {email}. {error}",
            "data": None
        }


def getPatientByEmail(email: str):
    """
    Get Patient by Email
    ====================
    Parameters:
    -----------
        email:
            description: Patient Email
            dtype: str
    -----------
    Returns:
    --------
        description: Success or Error Message
        dtype: dict
        Response Model: {
            "success": True or False,
            "message": Response Text,
            "data": object | None
        }
    """
    
    try:
        patient = models.Patient.objects.get(email=email)
        
        return {
            "success": True,
            "message": "Patient Found",
            "data": patient
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Error while getting patient with email: {email}. {error}",
            "data": None
        }


def getAllPractitioners():
    """
    Get All Practitioners
    =====================
    Parameters:
    -----------
        None
    -----------
    Returns:
    --------
        description: Success or Error Message
        dtype: dict
        Response Model: {
            "success": True or False,
            "message": Response Text,
            "data": list | None
        }
    """
    
    try:
        practitioners = models.Practitioner.objects.all()
        
        return {
            "success": True,
            "message": "All Practitioners",
            "data": practitioners
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Error while getting all practitioners. {error}",
            "data": None
        }


def getAllPatients():
    """
    Get All Patients
    =====================
    Parameters:
    -----------
        None
    -----------
    Returns:
    --------
        description: Success or Error Message
        dtype: dict
        Response Model: {
            "success": True or False,
            "message": Response Text,
            "data": list | None
        }
    """
    
    try:
        patients = models.Patient.objects.all()
        
        return {
            "success": True,
            "message": "All Patients",
            "data": patients
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Error while getting all patients. {error}",
            "data": None
        }


def addPractitioner(practitioner: schemas.User):
    """
    Add a new practitioner to the Database
    ======================================
    Parameters:
    -----------
        practitioner:
            description: Practitioner Object
            dtype: schemas.User
    -----------
    Returns:
    --------
        description: Success or Error Message
        dtype: dict
        Response Model: {
            "success": True or False,
            "message": Response Text,
            "data": object | None
        }
    """
    
    try:
        newUserID = uuid.uuid4()
        hashedPassword = security.getHashedPassword(practitioner.password)
        
        newPractitioner = models.Practitioner(
            id=newUserID,
            email=practitioner.email,
            password=hashedPassword,
            firstName=practitioner.firstName,
            lastName=practitioner.lastName,
            age=practitioner.age,
            dob=practitioner.dob,
            gender=practitioner.gender,
            phone=practitioner.phone,
            avatar=practitioner.avatar,
            address=practitioner.address
        )
        
        newPractitioner.save()
        
        return {
            "success": True,
            "message": "Practitioner Added",
            "data": newPractitioner
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Error while adding new practitioner. {error}",
            "data": None
        }


def addPatient(patient: schemas.User):
    """
    Add a new patient to the Database
    =================================
    Parameters:
    -----------
        patient:
            description: Patient Object
            dtype: schemas.User
    -----------
    Returns:
    --------
        description: Success or Error Message
        dtype: dict
        Response Model: {
            "success": True or False,
            "message": Response Text,
            "data": object | None
        }
    """
    
    try:
        newUserID = uuid.uuid4()
        hashedPassword = security.getHashedPassword(patient.password)
        
        newPatient = models.Patient(
            id=newUserID,
            email=patient.email,
            password=hashedPassword,
            firstName=patient.firstName,
            lastName=patient.lastName,
            age=patient.age,
            dob=patient.dob,
            gender=patient.gender,
            phone=patient.phone,
            avatar=patient.avatar,
            address=patient.address
        )
        
        newPatient.save()
        
        return {
            "success": True,
            "message": "Patient Added",
            "data": newPatient
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Error while adding new patient. {error}",
            "data": None
        }


def assignPatientToPractitioner(practitionerID: str, patientID: str):
    """
    Assign a patient to a practitioner
    ==================================
    Parameters:
    -----------
        practitionerID:
            description: Practitioner ID
            dtype: str
        patientID:
            description: Patient ID
            dtype: str
    -----------
    Returns:
    --------
        description: Success or Error Message
        dtype: dict
        Response Model: {
            "success": True or False,
            "message": Response Text,
            "data": object | None
        }
    """
    
    try:
        practitioner = models.Practitioner.objects.get(id=practitionerID)
        patient = models.Patient.objects.get(id=patientID)
        
        practitioner.patients.add(patient)
        
        return {
            "success": True,
            "message": "Patient Assigned to Practitioner",
            "data": practitioner
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Error while assigning patient to practitioner. {error}",
            "data": None
        }


def assignDiseaseToPatient(patientID: str, diseaseID: str):
    """
    Assign a disease to a patient
    =============================
    Parameters:
    -----------
        patientID:
            description: Patient ID
            dtype: str
        diseaseID:
            description: Disease ID
            dtype: str
    -----------
    Returns:
    --------
        description: Success or Error Message
        dtype: dict
        Response Model: {
            "success": True or False,
            "message": Response Text,
            "data": object | None
        }
    """
    
    try:
        patient = models.Patient.objects.get(id=patientID)
        disease = models.Disease.objects.get(id=diseaseID)
        
        patient.diseases.add(disease)
        
        return {
            "success": True,
            "message": "Disease Assigned to Patient",
            "data": patient
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Error while assigning disease to patient. {error}",
            "data": None
        }