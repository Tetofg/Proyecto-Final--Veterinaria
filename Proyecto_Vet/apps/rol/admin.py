from multiprocessing.connection import Client
from django.contrib import admin

from .models import Adopcion, Category, Detdop, Mascotas

admin.site.register(Category)
admin.site.register(Mascotas)
admin.site.register(Adopcion)
admin.site.register(Detdop)



