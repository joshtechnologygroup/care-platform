# Generated by Django 2.2.11 on 2020-05-27 08:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0007_care_platform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facilitystaff",
            name="email",
            field=models.EmailField(
                help_text="email of the facility staff",
                max_length=50,
                validators=[django.core.validators.EmailValidator],
            ),
        ),
        migrations.AlterField(
            model_name="facilitystaff",
            name="phone_number",
            field=models.CharField(
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
            ),
        ),
    ]
