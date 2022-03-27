from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('maccs/', admin.site.urls),
    path('', include("apps.portfolio.urls"))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Krystian Maccs Admin"
admin.site.site_title = "Krystian Maccs Admin Portal"
admin.site.index_title = "Welcome to Krystian Maccs' Portal"