from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoryView()),
    path('binary/<str:id>', views.DocumentDownloaderView),
    path('<str:id>', views.DocumentView()),
    path('', views.DefaultView()),
]
