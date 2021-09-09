# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .models import socios
# from django.core.mail import send_mail, EmailMessage
# from django.conf import settings
# from django.contrib.postgres.search import SearchQuery, SearchVector
# from .utils import render_to_pdf
# from django.contrib.auth.models import User
# # Create your views here.
from rest_framework import  viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import calcular_edad
from datetime import datetime
from Socios.models import socios, familiar
from Socios.serializers import SociosSerializer, FamiliarSerializer



class SociosViewSet(viewsets.ModelViewSet):
    serializer_class = SociosSerializer
    queryset = socios.objects.all()

    def perform_create(self, serializers):
        _edad = calcular_edad(datetime.strptime(self.request.POST['fecha_nacimiento'],'%Y-%m-%d'))
        serializers.save(edad=_edad)
        
    def perform_update(self, serializers):
        _edad = calcular_edad(datetime.strptime(self.request.POST['fecha_nacimiento'],'%Y-%m-%d'))
        serializers.save(edad=_edad)


class FamiliarViewSet(viewsets.ModelViewSet):
    serializer_class = FamiliarSerializer
    queryset = familiar.objects.all()

    def perform_create(self, serializers):
        _edad = calcular_edad(datetime.strptime(self.request.POST['fecha_nacimiento'],'%Y-%m-%d'))
        serializers.save(edad=_edad)
        
    def perform_update(self, serializers):
        _edad = calcular_edad(datetime.strptime(self.request.POST['fecha_nacimiento'],'%Y-%m-%d'))
        serializers.save(edad=_edad)


# """
# Funcion que recibira los datos del formulario
# de inscripcion del socio y enviarlos por mail
# """
# def inscrib_socio(request):    
#     if request.method=='POST':
#         mi_formulario=form_inscripcion(request.POST)
#         if mi_formulario.is_valid():
#             ape_nomb=request.POST.get('apellido_nombre')
#             _dni=request.POST.get('dni')
#             _calle=request.POST.get('calle')
#             _localidad=request.POST.get('localidad')
#             depto=request.POST.get('departamento')
#             cod_postal=request.POST.get('cod_postal')
#             fech_nac=request.POST.get('fecha_nacimiento')
#             age=request.POST.get('edad')
#             #carencia=forms.DateField(label="Carencia")
#             _email=request.POST.get('email')
#             tel_f=request.POST.get('tel_fijo')
#             tel_c=request.POST.get('tel_celular')
#             #imagedni=request.POST.get('imagen_dni')


#             _mail=EmailMessage("Solicitud de Inscripcion: ",
#             "-Nombre Completo: {}\n-DNI: {}\n-Domicilio: {} - {} - {}\n-Codigo Postal: {}\n-Fecha de Nacimiento: {}\n-Edad: {} Años\n-Correo: {}\n-Telefono Fijo: {}\n-Telefono Celular: {}" .format(ape_nomb,_dni,_calle,_localidad,depto,cod_postal,fech_nac,age,_email,tel_f,tel_c), "",
#             [settings.EMAIL_HOST_USER],reply_to=[_email])
            
#             try:
#                 _mail.send()
#                 return redirect("/socios/inscripcion/?valido")
#             except:
#                 return redirect("/socios/inscripcion/?novalido")
#     else:
#         mi_formulario=form_inscripcion()
    
#     return render(request, "socios/ins_socios.html", {"form": mi_formulario})

# """
# Funcion que leera y mostrara todos los datos de los socios en una tabla
# """
# def listado_socios(request):
#     #_socios = socios.objects.all()
#     _socios = socios.objects.order_by('numero_socio')
#     #_socios = socios.objects.get(numero_socio=id)
#     return render(request,"socios/list_socios.html", {"socios": _socios})


# """
# Funcion que leera y mostrara todos los datos de los socios en un pdf
# """
# def listado_socios_pdf(request):
#     _socios = socios.objects.all()

#     if User.is_authenticated:
#         pdf = render_to_pdf("socios/list_socios.html", {"socios": _socios})
#     return HttpResponse(pdf, content_type='application/pdf')

# """
# Funcion para buscar un empleado
# """
# def buscar_socio(request):
#     if request.GET['value']:
#         mensaje = "Buscando los registros: %r" %request.GET['value']

#         """
#         Aca hago un filtrado solamente por el numero de socio
#         #SELECT * FROM socios WHERE apellido_y_nombre LIKE '%request.GET['prod']%'
#         #datos = socios.objects.filter(numero_socio__icontains=request.GET['value'])
#         """
#         """
#         Aca hago un filtrado por los campos numero del socio, apellido y nombre, dni,
#         fecha de nacimiento y localidad
#         """
#         datos=socios.objects.annotate(search=SearchVector('numero_socio', 'apellido_y_nombre','dni','fecha_nacimiento','localidad')).filter(search=SearchQuery(request.GET['value']))
#         return render(request, "socios/resultBusqueda.html", {"date_soc": datos})

# """
# Funcion para dar de alta al socio, es decir, cargar
# los datos a la base de datos
# """
# """"
# def alta_socio(request):
#     mensaje=""    
#     if request.method=='POST':
#         mi_formulario=form_alta(request.POST)
#         if mi_formulario.is_valid():
#             mi_formulario.save()
#             mensaje = "Los datos se han registrado exitosamente"
#             mi_formulario=form_alta()
#     else:
#         mensaje = "Por favor ingrese nuevamente los datos"
#         mi_formulario=form_alta()
    
#     return render(request, "socios/alta_socio.html", {"form": mi_formulario, "mensaje":mensaje})
# """

# def alta_socio(request):
#     if request.method=='POST':
#         mi_formulario=form_alta(request.POST)
#         if mi_formulario.is_valid():
#             try:
#                 mi_formulario.save()
#                 mi_formulario=form_alta()
#                 return redirect("/socios/altasocios/?valido")
#             except:
#                 return redirect("/socios/altasocios/?novalido")
    
#     mi_formulario=form_alta()
    
#     return render(request, "socios/alta_socio.html", {"form": mi_formulario})


# """
# Funcion para obtener el formulario con los datos 
# a modificar de un socio
# """
# def modificar_socio(request, numero_socio):
#     _socio= socios.objects.filter(pk=numero_socio).first()
#     mi_formulario=form_alta(instance=_socio)
#     return render(request, "socios/modificar_socio.html", {"form": mi_formulario, "persona":_socio})
    
   
# """
# Funcion para modificar los datos a un socio
# """
# def actualizar_socio(request, numero_socio):
#     _socio= socios.objects.get(pk=numero_socio)
    
#     if request.method=='POST':
#         mi_formulario=form_alta(request.POST, instance=_socio)
#         if mi_formulario.is_valid():
#             mi_formulario.save()
#             """
#             try:
#                 mi_formulario.save()
#                 #mi_formulario=form_alta()
#                 return redirect("/socios/actualizarsocios")
#             except:
#                 return redirect("/socios/modificarsocios")
#             """
    
#     __socios= socios.objects.all()
    
#     return render(request,"socios/list_socios.html", {"socios": __socios})

# """
# Funcion para eliminar los datos a un socio
# """

# def eliminar_socio(request, numero_socio):
#     _socio= socios.objects.get(pk=numero_socio)
#     if _socio:
#         _socio.delete()
#         return redirect("/socios/listsocios/")
#     _socio= socios.objects.all()
#     return render(request,"socios/list_socios.html", {"socios": _socio})

    
    