from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.DocumentCategoryView()),
    path('documents', views.DocumentView()),
]
