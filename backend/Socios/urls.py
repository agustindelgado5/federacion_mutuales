from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from  django.conf.urls.static import static

#app_name='socio'

urlpatterns = [
    path('', views.listado_socios , name="Socios"),
    path('inscripcion/', views.inscrib_socio , name="Inscripcion"),
    path('listsocios/', views.listado_socios , name="Listado"),
    path('listsociospdf/', views.listado_socios_pdf , name="PDF_Socios"),
    path('altasocios/', views.alta_socio , name="Alta"),
    path('modificarsocios/<int:numero_socio>/', views.modificar_socio , name="Modificar"),
    path('actualizarsocios/<int:numero_socio>/', views.actualizar_socio , name="Actualizar"),
    path('eliminarsocios/<int:numero_socio>/', views.eliminar_socio , name="Eliminar"),
    path('listsocios/buscsocios/', views.buscar_socio , name="Buscar"),
]