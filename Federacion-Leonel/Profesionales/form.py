from django import forms
from django.forms import widgets
from django.forms.forms import Form
from Federacion.deptos import deptos_tucuman, provincias
from .models import profesionales
import datetime
"""
class form_alta(forms.Form):
    apellido_nombre=forms.CharField(label='Apellido y Nombre',max_length=80)
    dni=forms.IntegerField(label='DNI', min_value=1000000, max_value=999999999)
    localidad=forms.CharField(label='Localidad',max_length=30)
    provincia=forms.ChoiceField(label='Provincia',choices=provincias)
    fecha_ingreso=forms.DateField(label="Fecha de Nacimiento")
    matricula=forms.IntegerField(label='Edad')
    email=forms.EmailField(label='E-mail', required=False)   
    tel_fijo=forms.IntegerField(label='Telefono Fijo')
    tel_celular=forms.IntegerField(label='Telefono Celular')
"""

class form_alta(forms.ModelForm):
    class Meta:
        model=profesionales
        fields= ['id_medico','apellido_y_nombre', 'dni',
        'domicilio','localidad','provincia','fecha_ingreso',
        'especialidad','email','tel_fijo','tel_celular', 'matricula']

        widgets={'fecha_ingreso': forms.DateInput(attrs={'type':'date'}),
        }

