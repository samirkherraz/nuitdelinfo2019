import django.views.static
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('nuitdelinfo.apps.rest.urls')),
    path('', include('nuitdelinfo.apps.webui.urls')),
]