from multiprocessing.connection import Client
from django.contrib import admin

from .models import Adopcion, Category, Mascotas

admin.site.register(Category)
admin.site.register(Mascotas)
admin.site.register(Adopcion)




