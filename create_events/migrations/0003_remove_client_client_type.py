# Generated by Django 4.0.4 on 2022-05-23 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_events', '0002_client_client_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_type',
        ),
    ]