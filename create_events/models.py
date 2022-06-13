from django.conf import settings
from django.db import models


class Client(models.Model):

    CLIENT_TYPE = [
        ('client_potentiel', 'CLIENT_POTENTIEL'),
        ('client_existant', 'CLIENT_EXISTANT')
    ]
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobil = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    date_create = models.DateField(auto_now_add=False)
    date_update = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacte_by')
    type = models.CharField(max_length=100, choices=CLIENT_TYPE)

    class Meta:
        unique_together = ('company_name', 'email')


class Contract(models.Model):
    signature_date = models.DateField(auto_now=True)
    event_name = models.CharField(max_length=150)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='existing_customer')
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sales_contact')
    start_date_event = models.DateField(auto_now_add=False)
    end_date_event = models.DateField(auto_now_add=False)
    status = models.BooleanField(max_length=15)
    amount = models.FloatField(max_length=20)
    payement_due = models.DateField(auto_now_add=False)


class Event(models.Model):

    STATU_TYPE = [
        ('a_venir', 'EVENEMENT A VENIR'),
        ('cloturer', 'CLOTURER'),
    ]

    event_name = models.CharField(max_length=150)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client')
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    support_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='support_user', null=True
    )
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='contract')
    note = models.TextField(max_length=1000)
    statu = models.CharField(max_length=100, choices=STATU_TYPE)
