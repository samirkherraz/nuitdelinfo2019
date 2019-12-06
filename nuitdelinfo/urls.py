import django.views.static
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/filedrop/', include('nuitdelinfo.apps.filedrop.urls')),
    path('api/procedure/', include('nuitdelinfo.apps.procedure.urls')),
    path('api/chat/', include('nuitdelinfo.apps.chat.urls')),
    path('api/plan/', include('nuitdelinfo.apps.plan.urls')),
    path('api/profile/', include('nuitdelinfo.apps.profile.urls')),
    path('', include('nuitdelinfo.apps.webui.urls')),
]