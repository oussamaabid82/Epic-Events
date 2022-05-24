# Generated by Django 4.0.4 on 2022-05-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_type',
            field=models.CharField(choices=[('client_potentiel', 'CLIENT_POTENTIEL'), ('client_existant', 'CLIENT_EXISTANT')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]