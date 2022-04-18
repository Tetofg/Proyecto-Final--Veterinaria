# Generated by Django 4.0.4 on 2022-04-15 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección'),
        ),
        migrations.AddField(
            model_name='user',
            name='date_birthday',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='user',
            name='dni',
            field=models.CharField(default=1, max_length=10, unique=True, verbose_name='DPI'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Masculino'), ('female', 'Femenino'), ('other', 'Otro')], default='male', max_length=10, verbose_name='Genero'),
        ),
    ]