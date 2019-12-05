from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoryView()),
    path('document', views.DocumentView()),
    path('', views.DefaultView()),
]
