from rest_framework import viewsets
from .models import AppointmentSlot, Appointment, Patient
from .serializers import AppointmentSlotSerializer, AppointmentSerializer, PatientSerializer

# Create your views here.

class AppointmentSlotViewSet(viewsets.ModelViewSet):
    queryset = AppointmentSlot.objects.all()
    serializer_class = AppointmentSlotSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
