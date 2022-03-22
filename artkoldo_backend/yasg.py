from django.urls import path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from artkoldo_backend import settings

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title='Artkoldo API',
            default_version='v1',
            description='Documentation',
        ),
        public=True,
        permission_classes=(permissions.AllowAny,)
    )
urlpatterns = [
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocumentation/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
