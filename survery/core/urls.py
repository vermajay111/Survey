# urls.py
from django.urls import path
from .views import driver_form

urlpatterns = [
    path('driver-form/', driver_form, name='driver_form'),
]
