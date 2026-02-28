# appointments/views.py
from rest_framework import viewsets, serializers
from django.db import transaction
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    # We remove the static queryset = Appointment.objects.all() 
    # and replace it with this dynamic function:
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        
        # If the user is not logged in, return nothing
        if not user.is_authenticated:
            return Appointment.objects.none()
            
        # If the user is an Admin, they can see everything
        if user.role == 'ADMIN' or user.is_superuser:
            return Appointment.objects.all()
            
        # If the user is a Doctor, they only see appointments assigned to them
        if user.role == 'DOCTOR':
            return Appointment.objects.filter(doctor__user=user)
            
        # Default: The user is a Patient. They only see their own appointments.
        return Appointment.objects.filter(patient=user)

    def perform_create(self, serializer):
        patient = self.request.user
        doctor = serializer.validated_data['doctor']
        appointment_date = serializer.validated_data['appointment_date']

        with transaction.atomic():
            existing_appointment = Appointment.objects.select_for_update().filter(
                doctor=doctor,
                appointment_date=appointment_date,
                status__in=['PENDING', 'CONFIRMED']
            ).exists()

            if existing_appointment:
                raise serializers.ValidationError({
                    "error": "This exact time slot is already booked for this doctor."
                })

            serializer.save(patient=patient)