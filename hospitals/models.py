# hospitals/models.py
from django.db import models
from django.conf import settings

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    # A department belongs to one hospital, but a hospital can have many departments
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=100) # e.g., Cardiology, Pediatrics

    def __str__(self):
        return f"{self.name} at {self.hospital.name}"

class DoctorProfile(models.Model):
    # Safely linking the doctor to our Custom User without triggering import errors!
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_profile')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='doctors')
    specialization = models.CharField(max_length=255)
    experience_years = models.IntegerField(default=0)

    def __str__(self):
        # We can access the user's first and last name through the OneToOne connection
        return f"Dr. {self.user.first_name} {self.user.last_name} - {self.specialization}"