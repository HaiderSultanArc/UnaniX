from django.db import models

# Create your models here.


class PractionerPatientLink(models.Model):
    class Meta:
        db_table = 'practitioner_patient_link'
        
    id                      = models.CharField(max_length=255, primary_key=True)
    practitioner_id         = models.ForeignKey("Practitioner", on_delete=models.CASCADE)
    patient_id              = models.ForeignKey("Patient", on_delete=models.CASCADE)



class PractitionerDiseaseLink(models.Model):
    class Meta:
        db_table = 'practitioner_disease_link'
        
    id                      = models.CharField(max_length=255, primary_key=True)
    practitioner_id         = models.ForeignKey("Practitioner", on_delete=models.CASCADE)
    disease_id              = models.ForeignKey("Disease", on_delete=models.CASCADE)


class PractitionerSymptomLink(models.Model):
    class Meta:
        db_table = 'practitioner_symptom_link'
        
    id                      = models.CharField(max_length=255, primary_key=True)
    practitioner_id         = models.ForeignKey("Practitioner", on_delete=models.CASCADE)
    symptom_id              = models.ForeignKey("Symptom", on_delete=models.CASCADE)
    

class PatientDiseaseLink(models.Model):
    class Meta:
        db_table = 'patient_disease_link'
        
    id                      = models.CharField(max_length=255, primary_key=True)
    patient_id              = models.ForeignKey("Patient", on_delete=models.CASCADE)
    disease_id              = models.ForeignKey("Disease", on_delete=models.CASCADE)


class PatientSymptomLink(models.Model):
    class Meta:
        db_table = 'patient_symptom_link'
        
    id                      = models.CharField(max_length=255, primary_key=True)
    patient_id              = models.ForeignKey("Patient", on_delete=models.CASCADE)
    symptom_id              = models.ForeignKey("Symptom", on_delete=models.CASCADE)
    

class User(models.Model):
    class Meta:
        db_table = 'user'
    
    id                      = models.CharField(max_length=255, primary_key=True)
    email                   = models.CharField(max_length=255)
    hashedPassword          = models.CharField(max_length=255)
    firstName               = models.CharField(max_length=255)
    lastName                = models.CharField(max_length=255)
    
    age                     = models.IntegerField(blank=True, null=True)
    dob                     = models.CharField(max_length=255, blank=True, null=True)
    gender                  = models.CharField(max_length=255, blank=True, null=True)
    phone                   = models.CharField(max_length=255, blank=True, null=True)
    avatar                  = models.CharField(max_length=255, blank=True, null=True)
    address                 = models.CharField(max_length=255, blank=True, null=True)
    
    disabled                = models.BooleanField(default=False)
    role                    = models.CharField(max_length=255)
    

class Practitioner(User):
    class Meta:
        db_table = 'practitioner'
        
    diseases                = models.ManyToManyField("Disease", through=PractitionerDiseaseLink)
    symptoms                = models.ManyToManyField("Symptom", through=PractitionerSymptomLink)
    practitioners           = models.ManyToManyField("Practitioner", through=PractionerPatientLink)



class Patient(User):
    class Meta:
        db_table = 'patient'
    
    diseases                = models.ManyToManyField("Disease", through=PatientDiseaseLink)
    symptoms                = models.ManyToManyField("Symptom", through=PatientSymptomLink)
    practitioners           = models.ManyToManyField("Practitioner", through=PractionerPatientLink)



# ----------------------------------------------------------------------------------------------------


class DiseaseSymptomLink(models.Model):
    class Meta:
        db_table = 'cd_disease_symptom_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    disease_id             = models.ForeignKey("Disease", on_delete=models.CASCADE)
    symptom_id             = models.ForeignKey("Symptom", on_delete=models.CASCADE)


class DiseaseCauseLink(models.Model):
    class Meta:
        db_table = 'cd_disease_cause_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    disease_id             = models.ForeignKey("Disease", on_delete=models.CASCADE)
    causes                 = models.ForeignKey("Cause", on_delete=models.CASCADE)


class DiseaseTreatmentPrincipleLink(models.Model):
    class Meta:
        db_table = 'cd_disease_treatment_principle_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    disease_id             = models.ForeignKey("Disease", on_delete=models.CASCADE)
    treatment_principle_id = models.ForeignKey("TreatmentPrinciple", on_delete=models.CASCADE)


class DiseaseDrugLink(models.Model):
    class Meta:
        db_table = 'cd_disease_drug_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    disease_id             = models.ForeignKey("Disease", on_delete=models.CASCADE)
    drug_id                = models.ForeignKey("Drug", on_delete=models.CASCADE)
    drug_dose              = models.CharField(max_length=255)


class DiseaseRegimentalTherapyLink(models.Model):
    class Meta:
        db_table = 'cd_disease_regimental_therapy_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    disease_id             = models.ForeignKey("Disease", on_delete=models.CASCADE)
    regimental_therapy_id  = models.ForeignKey("RegimentalTherapy", on_delete=models.CASCADE)


class DiseasePharmacoTherapyLink(models.Model):
    class Meta:
        db_table = 'cd_disease_pharmaco_therapy_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    disease_id             = models.ForeignKey("Disease", on_delete=models.CASCADE)
    pharmaco_therapy_id    = models.ForeignKey("PharmacoTherapy", on_delete=models.CASCADE)


class DiseaseDietLink(models.Model):
    class Meta:
        db_table = 'cd_disease_diet_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    disease_id             = models.ForeignKey("Disease", on_delete=models.CASCADE)
    diet_id                = models.ForeignKey("Diet", on_delete=models.CASCADE)
    diet_type              = models.CharField(max_length=255)
    diet_dose              = models.CharField(max_length=255, null=True)
    diet_usage_time        = models.CharField(max_length=255, null=True)
    diet_usage_with        = models.CharField(max_length=255, null=True)


class DiseasePreventionLink(models.Model):
    class Meta:
        db_table = 'cd_disease_prevention_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    disease_id             = models.ForeignKey("Disease", on_delete=models.CASCADE)
    prevention_id          = models.ForeignKey("Prevention", on_delete=models.CASCADE)


class DiseaseReferenceLink(models.Model):
    class Meta:
        db_table = 'cd_disease_reference_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    disease_id             = models.ForeignKey("Disease", on_delete=models.CASCADE)
    reference_id           = models.ForeignKey("Reference", on_delete=models.CASCADE)


class SymptomRegimentalTherapyLink(models.Model):
    class Meta:
        db_table = 'cd_symptom_regimental_therapy_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    symptom_id             = models.ForeignKey("Symptom", on_delete=models.CASCADE)
    regimental_therapy_id  = models.ForeignKey("RegimentalTherapy", on_delete=models.CASCADE)


class DrugPharmacoTherapyLink(models.Model):
    class Meta:
        db_table = 'cd_drug_pharmaco_therapy_link'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    description            = models.CharField(max_length=255)
    drug_id                = models.ForeignKey("Drug", on_delete=models.CASCADE)
    pharmaco_therapy_id    = models.ForeignKey("PharmacoTherapy", on_delete=models.CASCADE)


class Symptom(models.Model):
    class Meta:
        db_table = 'cd_symptoms'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255)
    name_persian           = models.CharField(max_length=255)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=255)
    icd_code               = models.CharField(max_length=255)
    
    diseases               = models.ManyToManyField("Disease", through=DiseaseSymptomLink)
    regimental_therapies   = models.ManyToManyField("RegimentalTherapy", through=SymptomRegimentalTherapyLink)


class Cause(models.Model):
    class Meta:
        db_table = 'cd_causes'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255)
    name_persian           = models.CharField(max_length=255)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=255)
    diseases               = models.ManyToManyField("Disease", through=DiseaseCauseLink)


class TreatmentPrinciple(models.Model):
    class Meta:
        db_table = 'cd_treatment_principles'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255)
    name_persian           = models.CharField(max_length=255)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=255)
    diseases               = models.ManyToManyField("Disease", through=DiseaseTreatmentPrincipleLink)


class Drug(models.Model):
    class Meta:
        db_table = 'cd_drugs'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255)
    name_persian           = models.CharField(max_length=255)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=255)
    
    diseases               = models.ManyToManyField("Disease", through=DiseaseDrugLink)
    pharmaco_therapies     = models.ManyToManyField("PharmacoTherapy", through=DrugPharmacoTherapyLink)


class RegimentalTherapy(models.Model):
    class Meta:
        db_table = 'cd_regimental_therapies'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255)
    name_persian           = models.CharField(max_length=255)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=255)
    
    diseases               = models.ManyToManyField("Disease", through=DiseaseRegimentalTherapyLink)
    symptoms               = models.ManyToManyField("Symptom", through=SymptomRegimentalTherapyLink)


class PharmacoTherapy(models.Model):
    class Meta:
        db_table = 'cd_pharmaco_therapies'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255)
    name_persian           = models.CharField(max_length=255)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=255)
    
    diseases               = models.ManyToManyField("Disease", through=DiseasePharmacoTherapyLink)
    drugs                  = models.ManyToManyField("Drug", through=DrugPharmacoTherapyLink)


class Diet(models.Model):
    class Meta:
        db_table = 'cd_diets'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255)
    name_persian           = models.CharField(max_length=255)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=255)
    diseases               = models.ManyToManyField("Disease", through=DiseaseDietLink)


class Prevention(models.Model):
    class Meta:
        db_table = 'cd_preventions'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255)
    name_persian           = models.CharField(max_length=255)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=255)
    diseases               = models.ManyToManyField("Disease", through=DiseasePreventionLink)


class Reference(models.Model):
    class Meta:
        db_table = 'cmn_references'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255)
    name_persian           = models.CharField(max_length=255)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=255)
    authors                = models.CharField(max_length=255)
    year                   = models.CharField(max_length=255)
    title                  = models.CharField(max_length=255)
    publisher              = models.CharField(max_length=255)
    edition                = models.CharField(max_length=255)
    volume                 = models.CharField(max_length=255)
    isbn                   = models.CharField(max_length=255)
    url                    = models.CharField(max_length=255)
    diseases               = models.ManyToManyField("Disease", through=DiseaseReferenceLink)


class Disease(models.Model):
    class Meta:
        db_table = 'cd_diseases'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255)
    name_persian           = models.CharField(max_length=255)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    icd_code               = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=255)
    
    symptoms               = models.ManyToManyField(Symptom,            through=DiseaseSymptomLink)
    causes                 = models.ManyToManyField(Cause,              through=DiseaseCauseLink)
    treatment_principles   = models.ManyToManyField(TreatmentPrinciple, through=DiseaseTreatmentPrincipleLink)
    drugs                  = models.ManyToManyField(Drug,               through=DiseaseDrugLink)
    regimental_therapies   = models.ManyToManyField(RegimentalTherapy,  through=DiseaseRegimentalTherapyLink)
    pharmaco_therapies     = models.ManyToManyField(PharmacoTherapy,    through=DiseasePharmacoTherapyLink)
    diets                  = models.ManyToManyField(Diet,               through=DiseaseDietLink)  
    preventions            = models.ManyToManyField(Prevention,         through=DiseasePreventionLink)  