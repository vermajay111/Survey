
from django.shortcuts import render, redirect
from .forms import DriverForm

def driver_form(request):
    if request.method == 'GET':
        form = DriverForm(request.GET)
        if form.is_valid():
            form.save()
            return render(request, 'driver_form.html', {'form': form})
    else:
        form = DriverForm()
    return render(request, 'driver_form.html', {'form': form})
