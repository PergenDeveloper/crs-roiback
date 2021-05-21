from django.conf import settings
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="CRS API",
      default_version='v1',
      description="Documentación de la API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include('core.bookings.urls')),
]

if settings.DEBUG:
    urlpatterns.append(
        path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    )
