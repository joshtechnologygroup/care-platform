# Generated by Django 2.2.11 on 2020-06-06 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0022_care_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpatient',
            name='patient_status',
            field=models.CharField(blank=True, choices=[(1, 'Home Isolation'), (2, 'Recovered'), (3, 'Dead'), (4, 'Facility Status')], max_length=25),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_status',
            field=models.CharField(blank=True, choices=[(1, 'Home Isolation'), (2, 'Recovered'), (3, 'Dead'), (4, 'Facility Status')], max_length=25),
        ),
    ]
