from datetime import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict
from Proyecto_Vet.settings import MEDIA_URL, STATIC_URL
from crum import get_current_request

class User(AbstractUser):
    dni = models.CharField(max_length=13, unique=True, verbose_name='DPI', )
    date_birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    gender = models.CharField(max_length=10, choices=(('male','Masculino'),('female','Femenino'),('other','Otro'),), default='male', verbose_name='Genero')
    image = models.ImageField(upload_to='user/%Y/%m/%d', null=True, blank=True)

    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)


    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(MEDIA_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['gender'] = self.get_gender_display()
        item['date_birthday'] = self.date_birthday.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item
    
    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass



