from datetime import datetime
from django.contrib.auth.models import Group

from django.forms import *

from apps.rol.models import Category, Mascotas, User, Adopcion


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class MascotasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Mascotas
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la mascota',
                }
            ),
            'cat': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'stock': TextInput(
                attrs={
                    'placeholder': '¿No Adoptado?',
                }
            ),
        }
        exclude = ['dpi']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'groups', 'email', 'dni', 'date_birthday', 'address', 'gender', 'password', 'image'
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
            'gender': Select(),
            'groups': SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'style': 'width: 100%',
                    'multiple': 'multiple'
                }
            )
        }

        exclude = ['user_permissions','last_login', 'is_superuser', 'is_staff', 
        'date_joined']

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
                u.groups.clear()
                for g in self.cleaned_data['groups']:
                    print(g.name)
                    u.groups.add(g)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned

class UserForm2(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'groups', 'email', 'dni', 'date_birthday', 'address', 'gender', 'password', 'image'
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
                    'readonly': 'readonly'
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
        }

        exclude = ['user_permissions','last_login', 'is_superuser', 'is_staff', 
        'date_joined','gender','groups']

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
                u.groups.clear()
                for g in self.cleaned_data['groups']:
                    print(g.name)
                    u.groups.add(g)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned


class UserProfileForm(ModelForm):
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
                    'readonly':'readonly',
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
                    'readonly':'readonly',
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
            'gender': Select(),
        }

        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff', 'groups']

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
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class AdopcionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Adopcion
        fields = 'first_name', 'last_name', 'dpi', 'motive', 'dire', 'pet'
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese su Apellido',
                }
            ),
            'dpi': NumberInput(
                attrs={
                    'placeholder': 'Ingrese su DPI',
                    'max':'9999999999999',
                    'min':'1000000000000'
                }
            ),
            'motive': TextInput(
                attrs={
                    'placeholder': 'Cuentenos mas acerca de su motivo de adopción',
                }
            ),
            'dire': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'pet': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            
        }
        exclude = ['date_adopt']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data