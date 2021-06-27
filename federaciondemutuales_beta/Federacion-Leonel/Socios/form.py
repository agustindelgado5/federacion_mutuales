from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.forms import Form
from Federacion.deptos import deptos_tucuman
from .models import socios
import datetime


class form_inscripcion(forms.Form):
    apellido_nombre=forms.CharField(label='Apellido y Nombre',max_length=80)
    dni=forms.IntegerField(label='DNI', min_value=1000000, max_value=999999999)
    calle=forms.CharField(label='Calle',max_length=50)
    localidad=forms.CharField(label='Localidad',max_length=30)
    departamento=forms.ChoiceField(label='Departamento',choices=deptos_tucuman)
    cod_postal=forms.IntegerField(label='Codigo Postal', min_value=1000, max_value=9999)
    fecha_nacimiento=forms.DateField(label="Fecha de Nacimiento")
    edad=forms.IntegerField(label='Edad')
    #carencia=forms.DateField(label="Carencia")
    email=forms.EmailField(label='E-mail')   
    tel_fijo=forms.IntegerField(label='Telefono Fijo')
    tel_celular=forms.IntegerField(label='Telefono Celular')
    imagen_dni=forms.ImageField(label='Foto del DNI', required=False)
     
    #mensaje=forms.CharField(label='Mensaje', max_length=100, widget=forms.Textarea)

"""
class form_alta(forms.Form):
    numero_socio=forms.IntegerField(label='N° Socio')
    apellido_nombre=forms.CharField(label='Apellido y Nombre',max_length=80)
    dni=forms.IntegerField(label='DNI', min_value=1000000, max_value=999999999)
    calle=forms.CharField(label='Calle',max_length=50)
    localidad=forms.CharField(label='Localidad',max_length=30)
    departamento=forms.ChoiceField(label='Departamento',choices=deptos_tucuman)
    cod_postal=forms.IntegerField(label='Codigo Postal', min_value=1000, max_value=9999)
    fecha_nacimiento=forms.DateField(label="Fecha de Nacimiento")
    edad=forms.IntegerField(label='Edad')
    
    email=forms.EmailField(label='E-mail')   
    tel_fijo=forms.IntegerField(label='Telefono Fijo')
    tel_celular=forms.IntegerField(label='Telefono Celular')
    carencia=forms.DateField(label="Carencia", required=False)
"""
class form_alta(forms.ModelForm):
    class Meta:
        model=socios
        fields= ['numero_socio','apellido_y_nombre', 'dni',
        'calle','localidad','departamento','cod_postal','fecha_nacimiento',
        'edad','email','tel_fijo','tel_celular', 'carencia']

        widgets={'fecha_nacimiento': forms.DateInput(attrs={'type':'date'}),
            'carencia': forms.DateInput(attrs={'type':'date'})
        }



    
  
  