from nuitdelinfo.urls import path
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
index = TemplateView.as_view(template_name='index.html')
urlpatterns = [
   
     path('', index,
         name='index'),
]
