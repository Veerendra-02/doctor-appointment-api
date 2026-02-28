# hospitals/admin.py
from django.contrib import admin
from .models import Hospital, Department, DoctorProfile

admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(DoctorProfile)