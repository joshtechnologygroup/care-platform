# Generated by Django 2.2.11 on 2020-05-26 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0007_care_platform'),
        ('patients', '0009_merge_20200524_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Rejected')], default=1)),
                ('status_updated_at', models.DateTimeField(blank=True, help_text='Date and time at wihich the status is updated', null=True)),
                ('comments', models.TextField(blank=True, help_text='comments related to patient transfer request', null=True)),
                ('from_patient_facility', models.ForeignKey(help_text='Current patient facility of a patient', on_delete=django.db.models.deletion.CASCADE, to='patients.PatientFacility')),
                ('to_facility', models.ForeignKey(help_text='New Facility in which the patient can be transferred', on_delete=django.db.models.deletion.CASCADE, to='facility.Facility')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
