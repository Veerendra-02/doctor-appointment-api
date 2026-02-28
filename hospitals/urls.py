# hospitals/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet, DepartmentViewSet, DoctorProfileViewSet

# A Router automatically generates the URL patterns for our ViewSets
router = DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'doctors', DoctorProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]