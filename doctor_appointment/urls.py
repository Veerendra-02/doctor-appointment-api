from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# This configures the title and description of your documentation homepage
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
    # ... keep your existing API paths here, exactly as you had them ...
    
    # This single line takes over the blank '404' root URL and turns it into the Swagger dashboard!
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]