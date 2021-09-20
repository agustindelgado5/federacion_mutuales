from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Profesionales.models import profesionales
from Profesionales.serializers import ProfesionalesSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


class ProfesionalesViewSet(viewsets.ModelViewSet):
    serializer_class = ProfesionalesSerializer
    queryset = profesionales.objects.all()


# from django.contrib.postgres import search
# from django.shortcuts import render, redirect
# from .form import  form_alta
# from .models import profesionales
# from django.conf import settings
# from django.contrib.postgres.search import SearchQuery, SearchVector
# # Create your views here.

# """
# Funcion que leera y mostrara todos los datos de los profesionales en una tabla
# """
# def listado_medicos(request):
#     #_medicos = profesionales.objects.all()
#     _medicos=profesionales.objects.order_by('id_medico')
#     return render(request,"profesionales/list_medico.html", {"medicos": _medicos})


# """
# Funcion para buscar un empleado
# """
# def buscar_medico(request):
#     if request.GET['value']:
#         """
#         Aca hago un filtrado por los campos numero del socio, apellido y nombre, dni,
#         fecha de nacimiento y localidad
#         """
#         datos=profesionales.objects.annotate(search=SearchVector('id_medico','apellido_y_nombre','matricula')).filter(search=SearchQuery(request.GET['value']))
#         return render(request, "profesionales/resultBusqueda.html", {"date_prof": datos})

# """
# Funcion para dar de alta al profesional, es decir, cargar
# los datos a la base de datos
# """

# def alta_medico(request):
#     if request.method=='POST':
#         mi_formulario=form_alta(request.POST)
#         if mi_formulario.is_valid():
#             try:
#                 mi_formulario.save()
#                 mi_formulario=form_alta()
#                 return redirect("/profesional/altamedico/?valido")
#             except:
#                 return redirect("/profesional/altamedico/?novalido")
#     else:
#         mi_formulario=form_alta()

#     return render(request, "profesionales/alta_medico.html", {"form": mi_formulario})

# """
# Funcion para obtener el formulario con los datos
# a modificar de un profesional
# """
# def modificar_medico(request, id_medico):
#     _medicos= profesionales.objects.filter(pk=id_medico).first()
#     mi_formulario=form_alta(instance=_medicos)
#     return render(request, "profesionales/modificar_medico.html", {"form": mi_formulario, "persona":_medicos})


# """
# Funcion para modificar los datos a un profesional
# """
# def actualizar_medico(request, id_medico):
#     _medico= profesionales.objects.get(pk=id_medico)

#     if request.method=='POST':
#         mi_formulario=form_alta(request.POST, instance=_medico)
#         if mi_formulario.is_valid():
#             mi_formulario.save()

#     __medicos= profesionales.objects.all()

#     return render(request,"profesionales/list_medico.html", {"medicos": __medicos})

# """
# Funcion para eliminar los datos a un profesional
# """

# def eliminar_medico(request, id_medico):
#     _medico= profesionales.objects.get(pk=id_medico)
#     if _medico:
#         _medico.delete()
#         return redirect("/profesional/listmedico/")
#     _medico= profesionales.objects.all()
#     return render(request,"profesionales/list_medico.html", {"medicos": _medico})
