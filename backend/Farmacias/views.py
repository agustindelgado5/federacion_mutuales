# from django.contrib.postgres import search
# from django.shortcuts import render, redirect
# from .form import form_alta
# from .models import farmacias
# from django.conf import settings
# from django.contrib.postgres.search import SearchQuery, SearchVector



# """
# Funcion que leera y mostrara todos los datos de las farmacias en una tabla
# """
# def listado_farmacias(request):
#     _farmacia = farmacias.objects.order_by('cod_farmacia')
#     return render(request,"farmacias/list_farm.html", {"farmacias": _farmacia})


# """
# Funcion para buscar un empleado
# """
# def buscar_farmacia(request):
#     if request.GET['value']:
#         datos=farmacias.objects.annotate(search=SearchVector('cod_farmacia', 'matricula_farm','farmacia','cuit')).filter(search=SearchQuery(request.GET['value']))
#         return render(request, "farmacias/resultBusqueda.html", {"date_farm": datos})

# """
# Funcion para dar de alta a la farmacia, es decir, cargar
# los datos a la base de datos
# """

# def alta_farmacia(request):
#     if request.method=='POST':
#         mi_formulario=form_alta(request.POST)
#         if mi_formulario.is_valid():
#             try:
#                 mi_formulario.save()
#                 mi_formulario=form_alta()
#                 return redirect("/farmacia/altafarm/?valido")
#             except:
#                 return redirect("/farmacia/altafarm/?novalido")
#     else:
#         mi_formulario=form_alta()
    
#     return render(request, "farmacias/alta_farm.html", {"form": mi_formulario})


# """
# Funcion para obtener el formulario con los datos 
# a modificar de un socio
# """
# def modificar_farmacia(request, cod_farmacia):
#     _farmacia= farmacias.objects.filter(pk=cod_farmacia).first()
#     mi_formulario=form_alta(instance=_farmacia)
#     return render(request, "farmacias/modificar_farm.html", {"form": mi_formulario, "farmacia":_farmacia})
    
   
# """
# Funcion para modificar los datos a un socio
# """
# def actualizar_farmacia(request, cod_farmacia):
#     _farmacia= farmacias.objects.get(pk=cod_farmacia)
    
#     if request.method=='POST':
#         mi_formulario=form_alta(request.POST, instance=_farmacia)
#         if mi_formulario.is_valid():
#             mi_formulario.save()
#     __farmacias= farmacias.objects.all()
    
#     return render(request,"farmacias/list_farm.html", {"farmacias": __farmacias})

# """
# Funcion para eliminar los datos a un socio
# """

# def eliminar_farmacia(request, cod_farmacia):
#     _farmacia= farmacias.objects.get(pk=cod_farmacia)
#     if _farmacia:
#         _farmacia.delete()
#         return redirect("/farmacia/listfarm/")
#     _farmacia= farmacias.objects.all()
#     return render(request,"farmacias/list_farm.html", {"farmacias": _farmacia})

    
    