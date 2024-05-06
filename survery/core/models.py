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
    interested_in_fitness = models.BooleanField(default=False, verbose_name="Are you interested in fitness and exercise?")
    enjoy_cooking = models.BooleanField(default=False, verbose_name="Do you enjoy cooking at home?")
    prefer_reading_fiction = models.BooleanField(default=False, verbose_name="Do you prefer reading fiction over non-fiction?")
    pet_owner = models.BooleanField(default=False, verbose_name="Are you a pet owner?")
    enjoy_outdoor_activities = models.BooleanField(default=False, verbose_name="Do you enjoy outdoor activities like hiking or camping?")
    morning_person = models.BooleanField(default=False, verbose_name="Are you a morning person?")
    tech_savvy = models.BooleanField(default=False, verbose_name="Do you consider yourself a tech-savvy person?")
    enjoy_scifi_movies = models.BooleanField(default=False, verbose_name="Are you a fan of science fiction movies?")
    prefer_texting_over_calling = models.BooleanField(default=False, verbose_name="Do you prefer texting over calling?")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
