from django.db import models
from django.contrib.auth.models import AbstractUser


class User_crm(AbstractUser):

    TEAM_CHOICES = [
        ('sales', 'SALES'),
        ('support', 'SUPPORT'),
        ('management', 'MANAGEMENT'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    team = models.CharField(max_length=32, choices=TEAM_CHOICES)
