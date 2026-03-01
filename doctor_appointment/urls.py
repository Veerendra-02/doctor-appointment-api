from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Hospital Booking API",
      default_version='v1',
      description="A highly concurrent REST API for managing hospital appointments, doctors, and patient records.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- YOUR ORIGINAL API ROUTES ---
    # (Change 'hospitals.urls' and 'appointments.urls' if your apps are named differently!)
    path('api/', include('hospitals.urls')),
    path('api/', include('appointments.urls')),
    
    # --- THE NEW SWAGGER HOMEPAGE ---
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]