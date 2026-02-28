# appointments/models.py
from django.db import models
from django.conf import settings
from hospitals.models import DoctorProfile

class Appointment(models.Model):
    # Defining the states an appointment can be in
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

    # Link to the Patient (User)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    
    # Link to the Doctor
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='appointments')
    
    appointment_date = models.DateTimeField()
    reason_for_visit = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment: {self.patient.username} with Dr. {self.doctor.user.last_name} on {self.appointment_date}"