
from django.contrib.auth.models import Group
from apps.rol.models import User
from django.forms import *
from datetime import datetime
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class NewUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
        self.fields['password'].validators.append(validate_password_strength)

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
                a.groups.add(Group.objects.get(name='Adoptante'))
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

def validate_password_strength(value):
    """Validates that a password is as least 7 characters long and has at least
    1 digit and 1 letter.
    """
    min_length = 12

    if len(value) < min_length:
        raise ValidationError(_('La contraseña debe tener al menos {0} caracteres '
                                'de largo.').format(min_length))

    # check for digit
    if not any(char.isdigit() for char in value):
        raise ValidationError(_('La contraseña debe contener al menos 1 dígito.'))

    # check for letter
    if not any(char.isalpha() for char in value):
        raise ValidationError(_('La contraseña debe contener al menos 1 letra.'))

    if not re.findall('[A-Z]', value):
            raise ValidationError(
                _("La contraseña debe contener al menos 1 letra mayúscula, A-Z."),
                code='password_no_upper',
            )