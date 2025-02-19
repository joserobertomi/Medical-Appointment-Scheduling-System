from django.urls import path, include
from rest_framework import routers
from .views import PatientViewSet, AppointmentViewSet, AppointmentSlotViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'appointment-slots', AppointmentSlotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]