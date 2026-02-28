# appointments/serializers.py
from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    # We grab the doctor's username and department to make the JSON readable
    doctor_name = serializers.CharField(source='doctor.user.username', read_only=True)
    department = serializers.CharField(source='doctor.department.name', read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id', 'doctor', 'doctor_name', 'department', 
            'appointment_date', 'reason_for_visit', 'status'
        ]
        # We don't want users to manually type in their own status when booking
        read_only_fields = ['status']