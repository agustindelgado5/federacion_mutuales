from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from  django.conf.urls.static import static

#app_name='medico'

urlpatterns = [
    path('', views.listado_medicos , name="Profesionales"),
    path('listmedico/', views.listado_medicos , name="Listado_Med"),
    path('altamedico/', views.alta_medico , name="Alta_Med"),
    path('listmedico/buscmedico/', views.buscar_medico , name="Buscar_Med"),
    path('modificarmedicos/<int:id_medico>/', views.modificar_medico , name="Modificar_Med"),
    path('actualizarmedicos/<int:id_medico>/', views.actualizar_medico , name="Actualizar_Med"),
    path('eliminarmedicos/<int:id_medico>/', views.eliminar_medico , name="Eliminar_Med"),
]