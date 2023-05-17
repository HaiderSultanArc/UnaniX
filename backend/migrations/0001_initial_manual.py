# Generated by Django 4.1.6 on 2023-03-20 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_persian', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('name_urdu_roman', models.CharField(max_length=255, null=True)),
                ('name_arabic', models.CharField(max_length=255, null=True)),
                ('name_hindi', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cd_causes',
            },
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_persian', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('name_urdu_roman', models.CharField(max_length=255, null=True)),
                ('name_arabic', models.CharField(max_length=255, null=True)),
                ('name_hindi', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cd_diets',
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_persian', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('name_urdu_roman', models.CharField(max_length=255, null=True)),
                ('name_arabic', models.CharField(max_length=255, null=True)),
                ('name_hindi', models.CharField(max_length=255, null=True)),
                ('icd_code', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cd_diseases',
            },
        ),
        migrations.CreateModel(
            name='DiseaseDrugLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('drug_dose', models.CharField(max_length=255)),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.disease')),
            ],
            options={
                'db_table': 'cd_disease_drug_link',
            },
        ),
        migrations.CreateModel(
            name='DiseasePharmacoTherapyLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.disease')),
            ],
            options={
                'db_table': 'cd_disease_pharmaco_therapy_link',
            },
        ),
        migrations.CreateModel(
            name='DiseasePreventionLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.disease')),
            ],
            options={
                'db_table': 'cd_disease_prevention_link',
            },
        ),
        migrations.CreateModel(
            name='DiseaseReferenceLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.disease')),
            ],
            options={
                'db_table': 'cd_disease_reference_link',
            },
        ),
        migrations.CreateModel(
            name='DiseaseRegimentalTherapyLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.disease')),
            ],
            options={
                'db_table': 'cd_disease_regimental_therapy_link',
            },
        ),
        migrations.CreateModel(
            name='DiseaseSymptomLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.disease')),
            ],
            options={
                'db_table': 'cd_disease_symptom_link',
            },
        ),
        migrations.CreateModel(
            name='DiseaseTreatmentPrincipleLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.disease')),
            ],
            options={
                'db_table': 'cd_disease_treatment_principle_link',
            },
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_persian', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('name_urdu_roman', models.CharField(max_length=255, null=True)),
                ('name_arabic', models.CharField(max_length=255, null=True)),
                ('name_hindi', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('diseases', models.ManyToManyField(through='db.DiseaseDrugLink', to='db.disease')),
            ],
            options={
                'db_table': 'cd_drugs',
            },
        ),
        migrations.CreateModel(
            name='DrugPharmacoTherapyLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('drug_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.drug')),
            ],
            options={
                'db_table': 'cd_drug_pharmaco_therapy_link',
            },
        ),
        migrations.CreateModel(
            name='RegimentalTherapy',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_persian', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('name_urdu_roman', models.CharField(max_length=255, null=True)),
                ('name_arabic', models.CharField(max_length=255, null=True)),
                ('name_hindi', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('diseases', models.ManyToManyField(through='db.DiseaseRegimentalTherapyLink', to='db.disease')),
            ],
            options={
                'db_table': 'cd_regimental_therapies',
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_persian', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('name_urdu_roman', models.CharField(max_length=255, null=True)),
                ('name_arabic', models.CharField(max_length=255, null=True)),
                ('name_hindi', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('icd_code', models.CharField(max_length=255)),
                ('diseases', models.ManyToManyField(through='db.DiseaseSymptomLink', to='db.disease')),
            ],
            options={
                'db_table': 'cd_symptoms',
            },
        ),
        migrations.CreateModel(
            name='TreatmentPrinciple',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_persian', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('name_urdu_roman', models.CharField(max_length=255, null=True)),
                ('name_arabic', models.CharField(max_length=255, null=True)),
                ('name_hindi', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('diseases', models.ManyToManyField(through='db.DiseaseTreatmentPrincipleLink', to='db.disease')),
            ],
            options={
                'db_table': 'cd_treatment_principles',
            },
        ),
        migrations.CreateModel(
            name='SymptomRegimentalTherapyLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('regimental_therapy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.regimentaltherapy')),
                ('symptom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.symptom')),
            ],
            options={
                'db_table': 'cd_symptom_regimental_therapy_link',
            },
        ),
        migrations.AddField(
            model_name='symptom',
            name='regimental_therapies',
            field=models.ManyToManyField(through='db.SymptomRegimentalTherapyLink', to='db.regimentaltherapy'),
        ),
        migrations.AddField(
            model_name='regimentaltherapy',
            name='symptoms',
            field=models.ManyToManyField(through='db.SymptomRegimentalTherapyLink', to='db.symptom'),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_persian', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('name_urdu_roman', models.CharField(max_length=255, null=True)),
                ('name_arabic', models.CharField(max_length=255, null=True)),
                ('name_hindi', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=255)),
                ('volume', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('diseases', models.ManyToManyField(through='db.DiseaseReferenceLink', to='db.disease')),
            ],
            options={
                'db_table': 'cmn_references',
            },
        ),
        migrations.CreateModel(
            name='Prevention',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_persian', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('name_urdu_roman', models.CharField(max_length=255, null=True)),
                ('name_arabic', models.CharField(max_length=255, null=True)),
                ('name_hindi', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('diseases', models.ManyToManyField(through='db.DiseasePreventionLink', to='db.disease')),
            ],
            options={
                'db_table': 'cd_preventions',
            },
        ),
        migrations.CreateModel(
            name='PharmacoTherapy',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_persian', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('name_urdu_roman', models.CharField(max_length=255, null=True)),
                ('name_arabic', models.CharField(max_length=255, null=True)),
                ('name_hindi', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('diseases', models.ManyToManyField(through='db.DiseasePharmacoTherapyLink', to='db.disease')),
                ('drugs', models.ManyToManyField(through='db.DrugPharmacoTherapyLink', to='db.drug')),
            ],
            options={
                'db_table': 'cd_pharmaco_therapies',
            },
        ),
        migrations.AddField(
            model_name='drugpharmacotherapylink',
            name='pharmaco_therapy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.pharmacotherapy'),
        ),
        migrations.AddField(
            model_name='drug',
            name='pharmaco_therapies',
            field=models.ManyToManyField(through='db.DrugPharmacoTherapyLink', to='db.pharmacotherapy'),
        ),
        migrations.AddField(
            model_name='diseasetreatmentprinciplelink',
            name='treatment_principle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.treatmentprinciple'),
        ),
        migrations.AddField(
            model_name='diseasesymptomlink',
            name='symptom_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.symptom'),
        ),
        migrations.AddField(
            model_name='diseaseregimentaltherapylink',
            name='regimental_therapy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.regimentaltherapy'),
        ),
        migrations.AddField(
            model_name='diseasereferencelink',
            name='reference_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.reference'),
        ),
        migrations.AddField(
            model_name='diseasepreventionlink',
            name='prevention_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.prevention'),
        ),
        migrations.AddField(
            model_name='diseasepharmacotherapylink',
            name='pharmaco_therapy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.pharmacotherapy'),
        ),
        migrations.AddField(
            model_name='diseasedruglink',
            name='drug_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.drug'),
        ),
        migrations.CreateModel(
            name='DiseaseDietLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('diet_type', models.CharField(max_length=255)),
                ('diet_dose', models.CharField(max_length=255, null=True)),
                ('diet_usage_time', models.CharField(max_length=255, null=True)),
                ('diet_usage_with', models.CharField(max_length=255, null=True)),
                ('diet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.diet')),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.disease')),
            ],
            options={
                'db_table': 'cd_disease_diet_link',
            },
        ),
        migrations.CreateModel(
            name='DiseaseCauseLink',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('causes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.cause')),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.disease')),
            ],
            options={
                'db_table': 'cd_disease_cause_link',
            },
        ),
        migrations.AddField(
            model_name='disease',
            name='causes',
            field=models.ManyToManyField(through='db.DiseaseCauseLink', to='db.cause'),
        ),
        migrations.AddField(
            model_name='disease',
            name='diets',
            field=models.ManyToManyField(through='db.DiseaseDietLink', to='db.diet'),
        ),
        migrations.AddField(
            model_name='disease',
            name='drugs',
            field=models.ManyToManyField(through='db.DiseaseDrugLink', to='db.drug'),
        ),
        migrations.AddField(
            model_name='disease',
            name='pharmaco_therapies',
            field=models.ManyToManyField(through='db.DiseasePharmacoTherapyLink', to='db.pharmacotherapy'),
        ),
        migrations.AddField(
            model_name='disease',
            name='preventions',
            field=models.ManyToManyField(through='db.DiseasePreventionLink', to='db.prevention'),
        ),
        migrations.AddField(
            model_name='disease',
            name='regimental_therapies',
            field=models.ManyToManyField(through='db.DiseaseRegimentalTherapyLink', to='db.regimentaltherapy'),
        ),
        migrations.AddField(
            model_name='disease',
            name='symptoms',
            field=models.ManyToManyField(through='db.DiseaseSymptomLink', to='db.symptom'),
        ),
        migrations.AddField(
            model_name='disease',
            name='treatment_principles',
            field=models.ManyToManyField(through='db.DiseaseTreatmentPrincipleLink', to='db.treatmentprinciple'),
        ),
        migrations.AddField(
            model_name='diet',
            name='diseases',
            field=models.ManyToManyField(through='db.DiseaseDietLink', to='db.disease'),
        ),
        migrations.AddField(
            model_name='cause',
            name='diseases',
            field=models.ManyToManyField(through='db.DiseaseCauseLink', to='db.disease'),
        ),
    ]
