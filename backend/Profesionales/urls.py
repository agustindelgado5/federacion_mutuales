from django.urls import include, path

from rest_framework import routers

from . import views


# app_name='medico'

router = routers.DefaultRouter()
router.register(r"profesionales", views.ProfesionalesViewSet, basename="profesionales")


urlpatterns = [
    path("", include(router.urls)),
    # path('', views.listado_medicos , name="Profesionales"),
    # path('listmedico/', views.listado_medicos , name="Listado_Med"),
    # path('altamedico/', views.alta_medico , name="Alta_Med"),
    # path('listmedico/buscmedico/', views.buscar_medico , name="Buscar_Med"),
    # path('modificarmedicos/<int:id_medico>/', views.modificar_medico , name="Modificar_Med"),
    # path('actualizarmedicos/<int:id_medico>/', views.actualizar_medico , name="Actualizar_Med"),
    # path('eliminarmedicos/<int:id_medico>/', views.eliminar_medico , name="Eliminar_Med"),
]
