from django.db import models

class Driver(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    good_driver = models.BooleanField(default=False, verbose_name="Do you think you are a good driver?")
    speeding_ticket = models.BooleanField(default=False, verbose_name="Have you ever gotten a speeding ticket?")
    car_crash = models.BooleanField(default=False, verbose_name="Have you ever been in a car crash?")
    employed = models.BooleanField(default=False, verbose_name="Do you have a job?")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"