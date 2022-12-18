from django import forms
from usuarios.models import *
#from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.forms import ModelForm, TextInput, EmailInput

class UserRegisterForm(UserCreationForm):
    correo = forms.EmailField(label='Correo', widget=forms.EmailInput(
        attrs={'placeholder': 'Escriba su correo'}))
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
     #PUEDO USAR ESTE WIDGET SOLO EN EL ADMIN.SITE
     #el datepicker no se muestra en la vista
     #time_of_day = forms.DateField(widget=AdminDateWidget())
    class Meta:
        model = Usuario
        fields =['correo']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm,self).__init__(*args, **kwargs)
        self.fields['correo'].widget.attrs['class'] = 'form-control'

class InicioSessionForm(AuthenticationForm):
    username = forms.EmailField(label='Correo', widget=forms.EmailInput(
        attrs={'placeholder': 'Escriba su correo'}))
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
     #PUEDO USAR ESTE WIDGET SOLO EN EL ADMIN.SITE
     #el datepicker no se muestra en la vista
     #time_of_day = forms.DateField(widget=AdminDateWidget())
    class Meta:
        model = Usuario
        fields =['username']

    def __init__(self, *args, **kwargs):
        super(InicioSesionForm,self).__init__(*args, **kwargs)
        
        self.fields['usernasdme'].widget.attrs['class'] = 'form-control'

class InicioSesionForm(AuthenticationForm):
    username = forms.EmailField(label='Correo', widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder': 'Escriba su correo'}))
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Escriba su contraseña'}))

    class Meta:
        model = Usuario
        fields =['correo']

     #PUEDO USAR ESTE WIDGET SOLO EN EL ADMIN.SITE
     #el datepicker no se muestra en la vista
     #time_of_day = forms.DateField(widget=AdminDateWidget())
        # def __init__(self, *args, **kwargs):
        #     super(InicioSesionForm,self).__init__(*args, **kwargs)
        #     username = forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={'placeholder': 'Escriba su correo'}))
        #     print('asdsa')
        #     print(self.fields["username"].label)
        #     if self.fields["username"].label is None:
        #         self.fields["username"].label = capfirst(self.username_field.verbose_name)
        #         print(self.fields["username"].label)
