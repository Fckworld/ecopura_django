from django import forms
from ecopuraApp.models import Mensaje


class FormContacto(forms.ModelForm):
        #EN INIT ES CUANDO EMPIEZO A CUSTOMIZAR EL FORM CON FORMHELPER
        
        #LOS WIDGET ME PERMITEN AGREGAR CAMPOS DE HTML5
        p_nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
        p_apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
        empresa = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Empresa'}))
        telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono'}))
        rut_empresa = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Rut Empresa'}))
        rut_ver_empresa = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Codigo Verificador'}))
        correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Correo'}))
        CHOICES = (('BS', 'Básico'),('EL', 'Eléctrico'),('AB', 'Ambos'),)
        detalle_dispensador = forms.ChoiceField(choices=CHOICES)
        detalle_texto = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comentario'}))

            #ESTA MIERDE MUESTRA EL FORM Y QUE CAMPOS QUIERO MOSTRAR, PERO MEJOR LO HAGO EN VIEWS
