from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf.urls import url


schema_view = get_schema_view(
   openapi.Info(
      title="Krystian Maccs",
      default_version='v1',
      description="Krystian Maccs' Portfolio Website",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="krystianmaccs@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('maccs/', admin.site.urls),
    path("", include("apps.home.urls")),
    path("portfolio/", include("apps.portfolio.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Krystian Maccs Admin"
admin.site.site_title = "Krystian Maccs Admin Portal"
admin.site.index_title = "Welcome to Krystian Maccs' Portal"