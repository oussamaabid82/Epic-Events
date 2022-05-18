from django.conf import settings
from django.db import models


class Client(models.Model):
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    contact_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacte_by')
    contributor = models.ForeignKey('Contributor', on_delete=models.CASCADE, related_name='contributor')

    class Meta:
        unique_together = ('company_name', 'email')

class Contract(models.Model):
    signature_date = models.DateField(auto_now=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='existing_customer')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='event')
    

class Event(models.Model):
    event_name = models.CharField(max_length=150)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=False)
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='contract')
    contributor = models.ForeignKey('Contributor', on_delete=models.CASCADE, related_name='contributor_event')


class Contributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_contributor')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='event_contributor')
    
    class Meta:
        unique_together = ('user', 'client', 'event')
    
