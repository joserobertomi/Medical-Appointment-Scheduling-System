# Generated by Django 5.1.6 on 2025-02-19 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_id', models.CharField(max_length=10, unique=True)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'appointment_slot',
                'ordering': ['appointment_date', 'appointment_time'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('insurance', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'patient',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.CharField(max_length=10, unique=True)),
                ('scheduling_date', models.DateField()),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('scheduling_interval', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('check_in_time', models.TimeField(blank=True, null=True)),
                ('appointment_duration', models.DurationField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('waiting_time', models.DurationField(blank=True, null=True)),
                ('patient_id', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('age_group', models.CharField(max_length=10)),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.appointmentslot')),
            ],
            options={
                'db_table': 'appointment',
                'ordering': ['appointment_date', 'appointment_time'],
            },
        ),
    ]
