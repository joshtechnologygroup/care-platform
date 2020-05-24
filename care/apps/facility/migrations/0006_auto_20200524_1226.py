# Generated by Django 2.2.11 on 2020-05-24 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facility', '0005_auto_20200524_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='active',
        ),
        migrations.RemoveField(
            model_name='facilityinfrastructure',
            name='active',
        ),
        migrations.RemoveField(
            model_name='facilitytype',
            name='active',
        ),
        migrations.RemoveField(
            model_name='facilitytype',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='facilitytype',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='historicalinventory',
            name='active',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='active',
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='active',
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='testinglab',
            name='active',
        ),
        migrations.RemoveField(
            model_name='testinglab',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='testinglab',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='facilityinfrastructure',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalinventory',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventory',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='facility',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='HistoricalFacilityInfrastructure',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('total_bed', models.PositiveIntegerField(default=0)),
                ('occupied_bed', models.PositiveIntegerField(default=0)),
                ('available_bed', models.PositiveIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('bed_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='facility.BedType')),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='facility.Facility')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('room_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='facility.RoomType')),
            ],
            options={
                'verbose_name': 'historical facility infrastructure',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]