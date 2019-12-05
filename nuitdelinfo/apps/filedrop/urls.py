from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoryView()),
    path('', views.DefaultView()),
    path('<str:id>', views.DocumentView()),
]
