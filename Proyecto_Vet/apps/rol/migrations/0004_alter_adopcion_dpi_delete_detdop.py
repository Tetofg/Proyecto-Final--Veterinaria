# Generated by Django 4.0.4 on 2022-04-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0003_remove_adopcion_cli_adopcion_dire_adopcion_dpi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcion',
            name='dpi',
            field=models.CharField(max_length=13, unique=True, verbose_name='DPI'),
        ),
        migrations.DeleteModel(
            name='Detdop',
        ),
    ]
