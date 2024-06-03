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
    gun_control_support = models.BooleanField(default=False, verbose_name="Do you support stricter gun control laws?")
    abortion_rights_support = models.BooleanField(default=False, verbose_name="Do you believe in a woman's right to choose abortion?")
    death_penalty_support = models.BooleanField(default=False, verbose_name="Do you support the use of the death penalty for certain crimes?")
    immigration_policies_support = models.BooleanField(default=False, verbose_name="Do you support stricter immigration policies and border control?")
    affirmative_action_support = models.BooleanField(default=False, verbose_name="Do you support affirmative action policies to address discrimination and promote diversity?")
    climate_change_belief = models.BooleanField(default=False, verbose_name="Do you believe that climate change is primarily caused by human activities?")
    universal_basic_income_support = models.BooleanField(default=False, verbose_name="Do you support the implementation of a universal basic income for all citizens?")
    vaccination_mandates_support = models.BooleanField(default=False, verbose_name="Do you support mandatory vaccinations for children to attend school?")
    marijuana_legalization_support = models.BooleanField(default=False, verbose_name="Do you support the legalization of marijuana for recreational use?")
    censorship_laws_support = models.BooleanField(default=False, verbose_name="Do you believe in stricter censorship laws to regulate online content?")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
