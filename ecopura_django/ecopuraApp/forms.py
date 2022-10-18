from django import forms
from ecopuraApp.models import Mensaje
from ecopuraApp.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Field, Div, Column,Row
from django.core.validators import RegexValidator

def personal_validator(value):
    if len(value)<3:
        raise forms.ValidationError('el valor tiene que ser mayor a 3')

class CrearContactoForm(forms.ModelForm):
    #Tomar en cuenta que al usar el widget, el tipo de input predomina con el widget
    p_nombre = forms.CharField(max_length=100,label='Primer Nombre',widget=forms.TextInput(attrs={'placeholder':'Escriba su nombre'}))
    p_apellido = forms.CharField(max_length=100,label='Primer Apellido',widget=forms.TextInput(attrs={'placeholder':'Escriba su apellido'}))
    empresa = forms.CharField(max_length=100,label='Empresa',required=False,widget=forms.TextInput(attrs={'placeholder':'Opcional*'}))
    telefono = forms.IntegerField(label='Teléfono',widget=forms.NumberInput(attrs={'placeholder':'Ingresar número'}))
    rut_empresa = forms.CharField(max_length=13,label='Rut',required=False,validators=[RegexValidator(r'^\d\d.\d\d\d.\d\d\d-\d$',message='xx.xxx.xxx-x'),],widget=forms.TextInput(attrs={'placeholder':'Ingrese rut'}))
    #rut_ver_empresa = forms.CharField(max_length=1,label='',widget=forms.TextInput(attrs={'placeholder':'CV'}))
    correo = forms.EmailField(label='Correo')
    BASIC = 'BS'
    ELECTRIC = 'EL'
    AMBAS = 'AB'
    CHOICES = [
        (BASIC,'Básico'),
        (ELECTRIC,'Eléctrico'),
        (AMBAS,'Ambos',)
    ]
    detalle_dispensador = forms.CharField(label='Detalle Dispensador',widget=forms.Select(choices=CHOICES))
    detalle_texto = forms.CharField(label='Descripcion',widget=forms.TextInput(attrs={'placeholder':'Ingrese su comentario','style':'height:150px'}))

    class Meta:
        model = Mensaje
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        centrar = 'px-5 py-2 d-flex justify-content-center'
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        
        vl =  Div(
                    Div(
                        Field('p_nombre'),css_class=centrar,),
                    Div(
                        Field('p_apellido'),css_class=centrar,),
                    Div(
                        Field('empresa'),css_class=centrar,),
                    Div(
                        Field('telefono'),css_class=centrar,),
                    Div(
                        Field('rut_empresa'),css_class=centrar,),
                    Div(
                        Field('correo'),css_class=centrar,),
                    Div(
                        Field('detalle_dispensador'),css_class=centrar,),
                    Div(
                        Field('detalle_texto'),css_class=centrar,),

                    Submit('submit','Save',css_class=centrar,),
                    
                        
                    css_class='col bg-secondary rounded',css_id='columna_form',
        )
        self.helper.layout = Layout(vl)

    def clean_p_nombre(self, *args, **kwargs):
        p_nombre = self.cleaned_data.get('p_nombre')
        if len(p_nombre)>1:
            return p_nombre
        else:
            raise forms.ValidationError('ASDNJKLADHJKLS')
