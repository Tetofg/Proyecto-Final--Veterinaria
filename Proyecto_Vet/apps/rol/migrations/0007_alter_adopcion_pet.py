# Generated by Django 4.0.4 on 2022-04-20 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0006_remove_adopcion_pet_adopcion_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcion',
            name='pet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rol.mascotas'),
        ),
    ]
