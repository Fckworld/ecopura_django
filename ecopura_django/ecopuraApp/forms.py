from email import message
from django import forms
from ecopuraApp.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Field, Div, Column,Row
from django.core.validators import RegexValidator

class CrearContactoForm(forms.ModelForm):
    #Tomar en cuenta que al usar el widget, el tipo de input predomina con el widget
    p_nombre = forms.CharField(max_length=100,label='Primer Nombre',widget=forms.TextInput(attrs={'placeholder':'Escriba su nombre'}))
    p_apellido = forms.CharField(max_length=100,label='Primer Apellido',widget=forms.TextInput(attrs={'placeholder':'Escriba su apellido'}))
    empresa = forms.CharField(max_length=100,label='Empresa',required=False,widget=forms.TextInput(attrs={'placeholder':'Opcional*'}))
    telefono = forms.IntegerField(label='Teléfono',widget=forms.NumberInput(attrs={'placeholder':'Ingresar número'}))
    rut_empresa = forms.CharField(max_length=8,label='Rut',validators=[RegexValidator(message='mal formato')],widget=forms.TextInput(attrs={'placeholder':'Ingrese rut'}))
    rut_ver_empresa = forms.CharField(max_length=1,label='',widget=forms.TextInput(attrs={'placeholder':'Opcional*'}))
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

    class Meta:
        model = Mensaje
        exclude = ('usuario',)

    def __init__(self, *args, **kwargs):
        calzo = 'px-5 py-2'
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        
        vl =  Div(
                    Div(
                        Field('p_nombre'),css_class='px-5 py-2 pt-4',),
                    Div(
                        Field('p_apellido'),css_class=calzo,),
                    Div(
                        Field('empresa'),css_class='px-5 py-2',),
                    Div(
                        Field('telefono'),css_class='px-5 py-2',),
                    Div(
                        Field('rut_empresa'),css_class='px-5 py-2',),
                    Div(
                        Field('rut_ver_empresa'),css_class='px-5 py-2',),
                    Div(
                        Field('correo'),css_class='px-5 py-2',),
                    Div(
                        Field('detalle_dispensador'),css_class='px-5 py-2',),

                    Submit('submit','Enviar',css_class='my-5 mx-auto'),
                        
                    css_class='col bg-secondary rounded',css_id='columna_form',
        )
        self.helper.layout = Layout(vl)