from django.db import models

# Create your models here.

class AppointmentSlot(models.Model):
    slot_id = models.CharField(max_length=10, unique=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Slot {self.slot_id} - {self.appointment_date} {self.appointment_time} - {'Available' if self.is_available else 'Unavailable'}"
    
    class Meta:
        ordering = ['appointment_date', 'appointment_time']
        db_table = 'appointment_slot'


class Appointment(models.Model):
    appointment_id = models.CharField(max_length=10, unique=True)
    slot = models.ForeignKey(AppointmentSlot, on_delete=models.CASCADE)
    scheduling_date = models.DateField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    scheduling_interval = models.IntegerField()
    status = models.CharField(max_length=50)
    check_in_time = models.TimeField(null=True, blank=True)
    appointment_duration = models.DurationField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    waiting_time = models.DurationField(null=True, blank=True)
    patient_id = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    age_group = models.CharField(max_length=10)

    def __str__(self):
        return f"Appointment {self.appointment_id} - {self.appointment_date} {self.appointment_time} - Status: {self.status}"
    
    class Meta:
        ordering = ['appointment_date', 'appointment_time']
        db_table = 'appointment'
    

class Patient(models.Model):
    patient_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    dob = models.DateField()
    insurance = models.CharField(max_length=50)

    def __str__(self):
        return f"Patient {self.patient_id} - {self.name}"
    
    class Meta:
        ordering = ['name']
        db_table = 'patient'