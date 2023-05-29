from django.conf import settings
from django.contrib.auth.models import User
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


# ----------------------------------------------------------------------------------------------------


class CustomUser(User):
    ROLE_CHOICES = [
        ('practitioner', 'Practitioner'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=12, choices=ROLE_CHOICES)

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)

        if is_new:
            if self.role == 'practitioner':
                Practitioner.objects.create(user=self)
            elif self.role == 'patient':
                Patient.objects.create(user=self)

    @property
    def is_practitioner(self):
        return self.role == 'practitioner'

    @property
    def is_patient(self):
        return self.role == 'patient'


class Practitioner(models.Model):
    class Meta:
        db_table = 'practitioner'
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='practitioner')
    
    diseases                = models.ManyToManyField("Disease", through=PractitionerDiseaseLink)
    patients                = models.ManyToManyField("Patient", through=PractionerPatientLink)


class Patient(models.Model):
    class Meta:
        db_table = 'patient'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient')
    
    diseases                = models.ManyToManyField("Disease", through=PatientDiseaseLink)
    symptoms                = models.ManyToManyField("Symptom", through=PatientSymptomLink)
    practitioners           = models.ManyToManyField("Practitioner", through=PractionerPatientLink)


# ----------------------------------------------------------------------------------------------------


class DiseaseSymptomLink(models.Model):
    class Meta:
        db_table = 'disease_symptom_link'
    
    description            = models.CharField(max_length=1000, null=True)
    disease                = models.ForeignKey("Disease", on_delete=models.CASCADE)
    symptom                = models.ForeignKey("Symptom", on_delete=models.CASCADE)


class DiseaseCauseLink(models.Model):
    class Meta:
        db_table = 'disease_cause_link'
    
    description            = models.CharField(max_length=1000, null=True)
    disease                = models.ForeignKey("Disease", on_delete=models.CASCADE)
    cause                  = models.ForeignKey("Cause", on_delete=models.CASCADE)


class DiseaseTreatmentPrincipleLink(models.Model):
    class Meta:
        db_table = 'disease_treatment_principle_link'
    
    description            = models.CharField(max_length=1000, null=True)
    disease                = models.ForeignKey("Disease", on_delete=models.CASCADE)
    treatment_principle    = models.ForeignKey("TreatmentPrinciple", on_delete=models.CASCADE)


class DiseaseDrugLink(models.Model):
    class Meta:
        db_table = 'disease_drug_link'
    
    description            = models.CharField(max_length=1000, null=True)
    disease                = models.ForeignKey("Disease", on_delete=models.CASCADE)
    drug                   = models.ForeignKey("Drug", on_delete=models.CASCADE)
    drug_dose              = models.CharField(max_length=255, null=True)


class DiseaseRegimentalTherapyLink(models.Model):
    class Meta:
        db_table = 'disease_regimental_therapy_link'
    
    description            = models.CharField(max_length=1000, null=True)
    disease                = models.ForeignKey("Disease", on_delete=models.CASCADE)
    regimental_therapy     = models.ForeignKey("RegimentalTherapy", on_delete=models.CASCADE)


class DiseasePharmacoTherapyLink(models.Model):
    class Meta:
        db_table = 'disease_pharmaco_therapy_link'
    
    description            = models.CharField(max_length=1000, null=True)
    disease                = models.ForeignKey("Disease", on_delete=models.CASCADE)
    pharmaco_therapy       = models.ForeignKey("PharmacoTherapy", on_delete=models.CASCADE)


class DiseaseDietLink(models.Model):
    class Meta:
        db_table = 'disease_diet_link'
    
    description            = models.CharField(max_length=1000, null=True)
    disease                = models.ForeignKey("Disease", on_delete=models.CASCADE)
    diet                   = models.ForeignKey("Diet", on_delete=models.CASCADE)
    diet_type              = models.CharField(max_length=255)
    diet_dose              = models.CharField(max_length=255, null=True)
    diet_usage_time        = models.CharField(max_length=255, null=True)
    diet_usage_with        = models.CharField(max_length=255, null=True)


class DiseasePreventionLink(models.Model):
    class Meta:
        db_table = 'disease_prevention_link'
    
    description            = models.CharField(max_length=1000, null=True)
    disease                = models.ForeignKey("Disease", on_delete=models.CASCADE)
    prevention             = models.ForeignKey("Prevention", on_delete=models.CASCADE)


# class DiseaseReferenceLink(models.Model):
#     class Meta:
#         db_table = 'disease_reference_link'
    
#     id                     = models.CharField(max_length=255, primary_key=True)
#     description            = models.CharField(max_length=1000, null=True)
#     disease                = models.ForeignKey("Disease", on_delete=models.CASCADE)
#     reference              = models.ForeignKey("Reference", on_delete=models.CASCADE)


class SymptomRegimentalTherapyLink(models.Model):
    class Meta:
        db_table = 'symptom_regimental_therapy_link'
    
    description            = models.CharField(max_length=1000, null=True)
    symptom                = models.ForeignKey("Symptom", on_delete=models.CASCADE)
    regimental_therapy     = models.ForeignKey("RegimentalTherapy", on_delete=models.CASCADE)


class DrugPharmacoTherapyLink(models.Model):
    class Meta:
        db_table = 'drug_pharmaco_therapy_link'
    
    description            = models.CharField(max_length=1000, null=True)
    drug                   = models.ForeignKey("Drug", on_delete=models.CASCADE)
    pharmaco_therapy       = models.ForeignKey("PharmacoTherapy", on_delete=models.CASCADE)


class TreatmentPrinciple(models.Model):
    class Meta:
        db_table = 'treatment_principles'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255, unique=True)
    name_persian           = models.CharField(max_length=255, null=True)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=1000, null=True)
    diseases               = models.ManyToManyField("Disease", through=DiseaseTreatmentPrincipleLink)


class Drug(models.Model):
    class Meta:
        db_table = 'drugs'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255, unique=True)
    name_persian           = models.CharField(max_length=255, null=True)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=1000, null=True)
    
    diseases               = models.ManyToManyField("Disease", through=DiseaseDrugLink)
    pharmaco_therapies     = models.ManyToManyField("PharmacoTherapy", through=DrugPharmacoTherapyLink)


class RegimentalTherapy(models.Model):
    class Meta:
        db_table = 'regimental_therapies'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255, unique=True)
    name_persian           = models.CharField(max_length=255, null=True)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=1000, null=True)
    
    diseases               = models.ManyToManyField("Disease", through=DiseaseRegimentalTherapyLink)
    symptoms               = models.ManyToManyField("Symptom", through=SymptomRegimentalTherapyLink)


class PharmacoTherapy(models.Model):
    class Meta:
        db_table = 'pharmaco_therapies'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255, null=True)
    name_persian           = models.CharField(max_length=255, null=True)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=1000)
    
    diseases               = models.ManyToManyField("Disease", through=DiseasePharmacoTherapyLink)
    drugs                  = models.ManyToManyField("Drug", through=DrugPharmacoTherapyLink)


class Diet(models.Model):
    class Meta:
        db_table = 'diets'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255, unique=True)
    name_persian           = models.CharField(max_length=255, null=True)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=1000, null=True)
    diseases               = models.ManyToManyField("Disease", through=DiseaseDietLink)


class Prevention(models.Model):
    class Meta:
        db_table = 'preventions'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255, unique=True)
    name_persian           = models.CharField(max_length=255, null=True)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=1000, null=True)
    diseases               = models.ManyToManyField("Disease", through=DiseasePreventionLink)


# class Reference(models.Model):
#     class Meta:
#         db_table = 'cmn_references'
    
    
#     id                     = models.CharField(max_length=255, primary_key=True)
#     name_eng               = models.CharField(max_length=255, unique=True)
#     name_persian           = models.CharField(max_length=255, null=True)
#     name_urdu              = models.CharField(max_length=255, null=True)
#     name_urdu_roman        = models.CharField(max_length=255, null=True)
#     name_arabic            = models.CharField(max_length=255, null=True)
#     name_hindi             = models.CharField(max_length=255, null=True)
#     description            = models.CharField(max_length=1000, null=True)
#     authors                = models.CharField(max_length=255, unique=True)
#     year                   = models.CharField(max_length=255, unique=True)
#     title                  = models.CharField(max_length=255, unique=True)
#     publisher              = models.CharField(max_length=255, unique=True)
#     edition                = models.CharField(max_length=255, unique=True)
#     volume                 = models.CharField(max_length=255, unique=True)
#     isbn                   = models.CharField(max_length=255, unique=True)
#     url                    = models.CharField(max_length=255, unique=True)
#     diseases               = models.ManyToManyField("Disease", through=DiseaseReferenceLink)


class Symptom(models.Model):
    class Meta:
        db_table = 'symptoms'
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255, unique=True)
    name_persian           = models.CharField(max_length=255, null=True)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    icode                  = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=1000, null=True)
    
    diseases               = models.ManyToManyField("Disease", through=DiseaseSymptomLink)
    regimental_therapies   = models.ManyToManyField("RegimentalTherapy", through=SymptomRegimentalTherapyLink)


class Cause(models.Model):
    class Meta:
        db_table = 'causes'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255, unique=True)
    name_persian           = models.CharField(max_length=255, null=True)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=1000, null=True)
    diseases               = models.ManyToManyField("Disease", through=DiseaseCauseLink)


class Disease(models.Model):
    class Meta:
        db_table = 'diseases'
    
    
    id                     = models.CharField(max_length=255, primary_key=True)
    name_eng               = models.CharField(max_length=255, null=True)
    name_persian           = models.CharField(max_length=255, unique=True)
    name_urdu              = models.CharField(max_length=255, null=True)
    name_urdu_roman        = models.CharField(max_length=255, null=True)
    name_arabic            = models.CharField(max_length=255, null=True)
    name_hindi             = models.CharField(max_length=255, null=True)
    icode                  = models.CharField(max_length=255, null=True)
    description            = models.CharField(max_length=1000, null=True)
    
    symptoms               = models.ManyToManyField(Symptom,            through=DiseaseSymptomLink)
    causes                 = models.ManyToManyField(Cause,              through=DiseaseCauseLink)
    treatment_principles   = models.ManyToManyField(TreatmentPrinciple, through=DiseaseTreatmentPrincipleLink)
    drugs                  = models.ManyToManyField(Drug,               through=DiseaseDrugLink)
    regimental_therapies   = models.ManyToManyField(RegimentalTherapy,  through=DiseaseRegimentalTherapyLink)
    pharmaco_therapies     = models.ManyToManyField(PharmacoTherapy,    through=DiseasePharmacoTherapyLink)
    diets                  = models.ManyToManyField(Diet,               through=DiseaseDietLink)  
    preventions            = models.ManyToManyField(Prevention,         through=DiseasePreventionLink) 