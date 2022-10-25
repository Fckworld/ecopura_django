from django import forms
from ecopuraApp.models import Mensaje
from ecopuraApp.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Field, Div, Column, Row
from django.core.validators import RegexValidator


def personal_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('el valor tiene que ser mayor a 3')


class CrearContactoForm(forms.ModelForm):
    # Tomar en cuenta que al usar el widget, el tipo de input predomina con el widget
    p_nombre = forms.CharField(max_length=100, label='Nombre', widget=forms.TextInput(
        attrs={'placeholder': 'Escriba su nombre'}))
    p_apellido = forms.CharField(max_length=100, label='Apellido', widget=forms.TextInput(
        attrs={'placeholder': 'Escriba su apellido'}))
    empresa = forms.CharField(max_length=100, label='Empresa', required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Opcional*'}))
    telefono = forms.IntegerField(label='Teléfono', widget=forms.NumberInput(
        attrs={'placeholder': 'Ingresar número'}))
    rut_empresa = forms.CharField(max_length=13, label='Rut', required=False, validators=[RegexValidator(
        r'^\d\d.\d\d\d.\d\d\d-\d$', message='xx.xxx.xxx-x'), ], widget=forms.TextInput(attrs={'placeholder': 'Ingrese rut'}))
    #rut_ver_empresa = forms.CharField(max_length=1,label='',widget=forms.TextInput(attrs={'placeholder':'CV'}))
    correo = forms.EmailField(label='Correo')
    BASIC = 'BS'
    ELECTRIC = 'EL'
    AMBAS = 'AB'
    CHOICES = [
        (BASIC, 'Básico'),
        (ELECTRIC, 'Eléctrico'),
        (AMBAS, 'Ambos',)
    ]
    detalle_dispensador = forms.CharField(
        label='Detalle Dispensador', widget=forms.Select(choices=CHOICES))
    detalle_texto = forms.CharField(label='Descripcion', widget=forms.Textarea(
        attrs={'placeholder': 'Ingrese su comentario', 'style': 'height:150px','cols':"70", 'rows':'50'}))

    class Meta:
        model = Mensaje
        exclude = ('usuario','rut_ver_empresa',)

 
    def clean_p_nombre(self, *args, **kwargs):
        p_nombre = self.cleaned_data.get('p_nombre')
        if len(p_nombre) > 1:
            return p_nombre
        else:
            raise forms.ValidationError('ASDNJKLADHJKLS')