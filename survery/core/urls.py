# urls.py
from django.urls import path
from .views import driver_form, export_csv

urlpatterns = [
    path('', driver_form, name='driver_form'),
    path('export/', export_csv, name='driver_form'),
]
