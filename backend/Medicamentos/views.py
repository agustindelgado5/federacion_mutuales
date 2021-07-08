# from django.contrib.postgres import search
# from django.shortcuts import render, redirect
# from .form import form_alta
# from .models import medicamentos
# from django.conf import settings
# from django.contrib.postgres.search import SearchQuery, SearchVector
from rest_framework import  viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Medicamentos.models import medicamentos,receta
from Medicamentos.serializers import MedicamentosSerializer, RecetasSerializer


class MedicamentosViewSet(viewsets.ModelViewSet):
    serializer_class = MedicamentosSerializer
    queryset = medicamentos.objects.all()


class RecetasViewSet(viewsets.ModelViewSet):
    serializer_class = RecetasSerializer
    queryset = receta.objects.all()


# """
# Funcion que leera y mostrara todos los datos de los medicamentos en una tabla
# """
# def listado_medicamentos(request):
#     _medicamentos = medicamentos.objects.order_by('id_medicamento')
#     return render(request,"medicamentos/list_med.html", {"medicamentos": _medicamentos})


# """
# Funcion para buscar un medicamento
# """
# def buscar_medicamento(request):
#     if request.GET['value']:
#         datos=medicamentos.objects.annotate(search=SearchVector('id_medicamento','nombre','cod_farmacia')).filter(search=SearchQuery(request.GET['value']))
#         return render(request, "medicamentos/resultBusqueda.html", {"date_med": datos})

# """
# Funcion para dar de alta a un medicamento, es decir, cargar
# los datos a la base de datos
# """

# def alta_medicamento(request):
#     if request.method=='POST':
#         mi_formulario=form_alta(request.POST)
#         if mi_formulario.is_valid():
#             try:
#                 mi_formulario.save()
#                 mi_formulario=form_alta()
#                 return redirect("/medicamento/altamed/?valido")
#             except:
#                 return redirect("/medicamento/altamed/?novalido")
#     else:
#         mi_formulario=form_alta()
    
#     return render(request, "medicamentos/alta_med.html", {"form": mi_formulario})


# """
# Funcion para obtener el formulario con los datos 
# a modificar de un medicamento
# """
# def modificar_medicamento(request, id_medicamento):
#     _medicamento= medicamentos.objects.filter(pk=id_medicamento).first()
#     mi_formulario=form_alta(instance=_medicamento)
#     return render(request, "medicamentos/modificar_med.html", {"form": mi_formulario, "medicamento":_medicamento})
    
   
# """
# Funcion para modificar los datos a un medicamento
# """
# def actualizar_medicamento(request, id_medicamento):
#     _medicamento= medicamentos.objects.get(pk=id_medicamento)
    
#     if request.method=='POST':
#         mi_formulario=form_alta(request.POST, instance=_medicamento)
#         if mi_formulario.is_valid():
#             mi_formulario.save()
#     __medicamentos= medicamentos.objects.all()
    
#     return render(request,"medicamentos/list_med.html", {"medicamentos": __medicamentos})

# """
# Funcion para eliminar los datos a un medicamento
# """

# def eliminar_medicamento(request, id_medicamento):
#     _medicamento= medicamentos.objects.get(pk=id_medicamento)
#     if _medicamento:
#         _medicamento.delete()
#         return redirect("/medicamento/listmed/")
#     _medicamento= medicamentos.objects.all()
#     return render(request,"medicamentos/list_med.html", {"medicamentos": _medicamento})

    
    