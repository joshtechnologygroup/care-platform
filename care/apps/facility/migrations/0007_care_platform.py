# Generated by Django 2.2.11 on 2020-05-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0006_auto_20200524_1226"),
    ]

    operations = [
        migrations.AddField(
            model_name="testinglab",
            name="code",
            field=models.CharField(
                default=1,
                help_text="code of the Testing Lab",
                max_length=20,
                unique=True,
            ),
            preserve_default=False,
        ),
    ]
