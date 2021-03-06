# Generated by Django 2.2.11 on 2020-05-24 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patients", "0006_care_platform"),
    ]

    operations = [
        migrations.RenameField(
            model_name="historicalpatient",
            old_name="clinicals",
            new_name="clinical_status",
        ),
        migrations.RenameField(
            model_name="patient", old_name="clinicals", new_name="clinical_status",
        ),
        migrations.RemoveField(model_name="historicalpatient", name="home_isolation",),
        migrations.RemoveField(model_name="patient", name="home_isolation",),
        migrations.AddField(
            model_name="historicalpatient",
            name="patient_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("home-isolation", "Home Isolation"),
                    ("recovered", "Recovered"),
                    ("dead", "Dead"),
                    ("facility-status", "Facility Status"),
                ],
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="patient",
            name="patient_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("home-isolation", "Home Isolation"),
                    ("recovered", "Recovered"),
                    ("dead", "Dead"),
                    ("facility-status", "Facility Status"),
                ],
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="patientfacility",
            name="patient",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="patients.Patient",
            ),
            preserve_default=False,
        ),
    ]
