# hospitals/serializers.py
from rest_framework import serializers
from .models import Hospital, Department, DoctorProfile

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'  # This easily converts all columns in the table to JSON

class DepartmentSerializer(serializers.ModelSerializer):
    # We add this so the JSON shows the actual hospital name, not just its ID number
    hospital_name = serializers.CharField(source='hospital.name', read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'hospital', 'hospital_name']

class DoctorProfileSerializer(serializers.ModelSerializer):
    # Pulling the doctor's name directly from the linked Core User model
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = DoctorProfile
        fields = [
            'id', 'user', 'first_name', 'last_name', 
            'department', 'department_name', 
            'specialization', 'experience_years'
        ]