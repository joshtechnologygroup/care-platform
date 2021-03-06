# Generated by Django 2.2.11 on 2020-05-24 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patients", "0007_auto_20200524_2108"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientfacility",
            name="patient_status",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="patients.PatientStatus",
            ),
            preserve_default=False,
        ),
    ]
