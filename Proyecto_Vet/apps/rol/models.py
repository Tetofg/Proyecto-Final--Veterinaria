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

class Mascotas(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mascotas/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def __str__(self):
        return  self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        item['image'] = self.get_image()
        return item

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        ordering = ['id']


class Adopcion(models.Model):
    cli = models.ForeignKey(User, on_delete=models.CASCADE)
    date_adopt = models.DateField(default=datetime.now)
   
    def str(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Adopcion'
        verbose_name_plural = 'Adopciones'
        ordering = ['id']


class Detdop(models.Model):
    adoption = models.ForeignKey(Adopcion, on_delete=models.CASCADE)
    pet = models.ForeignKey(Mascotas, on_delete=models.CASCADE)
    raza= models.CharField(max_length=150, verbose_name='Raza')
    cant = models.IntegerField(default=0)
   

    def str(self):
        return self.pet.name

    class Meta:
        verbose_name = 'Detalle de adopcion'
        verbose_name_plural = 'Detalle de adopciones'
        ordering = ['id']