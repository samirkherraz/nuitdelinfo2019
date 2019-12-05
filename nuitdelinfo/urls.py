import django.views.static
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/filedrop/', include('nuitdelinfo.apps.filedrop.urls')),
    path('', include('nuitdelinfo.apps.webui.urls')),
]