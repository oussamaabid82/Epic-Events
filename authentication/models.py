from django.db import models
from django.contrib.auth.models import AbstractUser


class User_crm(AbstractUser):
    TEAM_CHOICES =[
        ('SALES', 'sales'),
        ('SUPPORT', 'support'),
        ('MANAGEMENT','management'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.CharField(max_length=32, choices=TEAM_CHOICES)
    
    
