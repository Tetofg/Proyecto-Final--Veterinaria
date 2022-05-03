from email.policy import default
from django.conf import settings
from django.db import models
from datetime import datetime

from django.forms import model_to_dict
from apps.user.models import User
from apps.models import BaseModel
from Proyecto_Vet.settings import MEDIA_URL, STATIC_URL
# from crum import get_current_user

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    des =  models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Vacunas(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    des =  models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Vacuna'
        verbose_name_plural = 'Vacunas'
        ordering = ['id']

class Mascotas(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mascotas/%Y/%m/%d', null=True, blank=True)
    sta = models.CharField(max_length=11, choices=(('in_adoption','En Adopcion'),('adopted','Adoptado'),), default='in_adoption', verbose_name='Estado')
    breed = models.CharField(max_length=150, verbose_name='Raza')
    rescue_date =  models.DateField(default=datetime.now, verbose_name='Fecha de Rescate')
    age = models.CharField(max_length=3, verbose_name='Edad')
    illness = models.CharField(max_length=250, verbose_name='Enfermedades Padecidas')
    food = models.CharField(max_length=250, verbose_name='Alimentación', default='Dog Chow')
    dpi = models.CharField(max_length=13, verbose_name='DPI')
    vaccine = models.ManyToManyField(Vacunas,verbose_name='Vacunas')
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def __str__(self):
        return  self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        item['vaccine'] = [{'id': g.id, 'name': g.name} for g in self.vaccine.all()]
        item['image'] = self.get_image()
        return item

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        ordering = ['id']


class Adopcion(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Nombres')
    last_name = models.CharField(max_length=150, verbose_name='Apellidos')
    dpi = models.CharField(max_length=13, verbose_name='DPI', unique=True)
    motive = models.CharField(max_length=250, verbose_name='Motivo')
    dire = models.CharField(max_length=50, verbose_name='Direccion')
    pet = models.OneToOneField(Mascotas, on_delete=models.CASCADE,verbose_name='Mascotas')
    date_adopt = models.DateField(default=datetime.now)
   
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Adopcion'
        verbose_name_plural = 'Adopciones'
        ordering = ['id']


