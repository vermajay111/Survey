from django.shortcuts import render, redirect
from .forms import DriverForm
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
from .models import Driver

def driver_form(request):
    if request.method == 'GET':
        form = DriverForm(request.GET)
        if form.is_valid():
            form.save()
            return render(request, 'done.html')
    else:
        form = DriverForm()
    return render(request, 'driver_form.html', {'form': form})

@login_required
def export_csv(request):
    # Get all objects from your model
    queryset = Driver.objects.all()

    # Define the response content type
    response = HttpResponse(content_type='text/csv')
    # Set the CSV file name
    response['Content-Disposition'] = 'attachment; filename="database_export.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write the header row
    writer.writerow([field.name for field in Driver._meta.fields])

    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field.name) for field in Driver._meta.fields])

    return response

