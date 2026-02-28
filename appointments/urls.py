# appointments/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet

router = DefaultRouter()
# This creates the /api/bookings/ endpoint
router.register(r'bookings', AppointmentViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]