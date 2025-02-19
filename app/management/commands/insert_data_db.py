import csv
from datetime import datetime, timedelta
from app.models import AppointmentSlot, Appointment, Patient
from datetime import datetime

from os import system 

def onde_eu_to():
    print(system('ls ./data'))

DATA_DIR = './data/'

def import_appointment_slots():
    data_path = DATA_DIR+'slots.csv'
    print(data_path)
    with open(data_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        slots = []
        for row in reader:
            slots.append(AppointmentSlot(
                slot_id=row['slot_id'],
                appointment_date=datetime.strptime(row['appointment_date'], '%Y-%m-%d').date(),
                appointment_time=datetime.strptime(row['appointment_time'], '%H:%M').time(),
                is_available=row['is_available'].lower() == 'true'
            ))

        # Inserção em lote para melhor performance
        AppointmentSlot.objects.bulk_create(slots, ignore_conflicts=True)

    print(f'{len(slots)} registros importados com sucesso!')

def import_appointments():
    with open('appointments.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        appointments = []

        for row in reader:
            try:
                slot = AppointmentSlot.objects.get(slot_id=row['slot_id'])

                appointment = Appointment(
                    appointment_id=row['appointment_id'],
                    slot=slot,
                    scheduling_date=datetime.strptime(row['scheduling_date'], '%Y-%m-%d').date(),
                    appointment_date=datetime.strptime(row['appointment_date'], '%Y-%m-%d').date(),
                    appointment_time=datetime.strptime(row['appointment_time'], '%H:%M').time(),
                    scheduling_interval=int(row['scheduling_interval']),
                    status=row['status'],
                    check_in_time=datetime.strptime(row['check_in_time'], '%H:%M').time() if row['check_in_time'] else None,
                    appointment_duration=timedelta(seconds=int(row['appointment_duration'].split(":")[0]) * 3600 +
                                                   int(row['appointment_duration'].split(":")[1]) * 60) if row['appointment_duration'] else None,
                    start_time=datetime.strptime(row['start_time'], '%H:%M').time() if row['start_time'] else None,
                    end_time=datetime.strptime(row['end_time'], '%H:%M').time() if row['end_time'] else None,
                    waiting_time=timedelta(seconds=int(row['waiting_time'].split(":")[0]) * 3600 +
                                           int(row['waiting_time'].split(":")[1]) * 60) if row['waiting_time'] else None,
                    patient_id=row['patient_id'],
                    sex=row['sex'],
                    age=int(row['age']),
                    age_group=row['age_group']
                )
                appointments.append(appointment)
            except AppointmentSlot.DoesNotExist:
                print(f"⚠️ Slot {row['slot_id']} não encontrado. Agendamento {row['appointment_id']} ignorado.")

        # Inserir em lote
        Appointment.objects.bulk_create(appointments)

    print(f'{len(appointments)} registros de Appointment importados com sucesso!')


def import_patients():
    with open('patients.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        patients = []

        for row in reader:
            patient = Patient(
                patient_id=row['patient_id'],
                name=row['name'],
                sex=row['sex'],
                dob=datetime.strptime(row['dob'], '%Y-%m-%d').date(),
                insurance=row['insurance']
            )
            patients.append(patient)

        # Inserção em lote para melhor performance
        Patient.objects.bulk_create(patients, ignore_conflicts=True)

    print(f'{len(patients)} registros de pacientes importados com sucesso!')
