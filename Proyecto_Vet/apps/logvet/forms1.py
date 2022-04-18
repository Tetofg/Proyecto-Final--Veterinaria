
from django.contrib.auth.models import Group
from apps.rol.models import User
from django.forms import *
from datetime import datetime

class NewUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'email', 'dni', 'date_birthday', 'address', 'gender', 'password', 'image'
        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese su Username',
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Ingrese su Correo',
                }
            ),
            'password': PasswordInput( render_value=True,
                attrs={
                    'placeholder': 'Ingrese su Contraseña',
                }
            ),
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                    'class': '',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'dni': NumberInput(
                attrs={
                    'placeholder': 'Ingrese su DPI',
                }
            ),
            'date_birthday': DateTimeInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'gender': Select()
        }

        exclude = ['user_permissions','last_login', 'is_superuser', 'is_staff', 
        'date_joined', 'groups']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
                a = form.save(commit=False)
                a.groups.add(Group.objects.get(name='Adoptantes'))
                a.save_m2m()
            else:
                data['error'] = form.errors
            # if form.is_valid():
            #     a = form.save(commit=False)
            #     a.groups.add(Group.objects.get(name='Adoptantes'))
            #     a.save_m2m()
        except Exception as e:
            pass
            #data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned