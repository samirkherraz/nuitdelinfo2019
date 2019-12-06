from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryView()),
    path('document/<str:id>/', views.DocumentView()),
    path('constraint/<str:id>/', views.ConstraintView()),
    path('', views.DefaultView()),
]
