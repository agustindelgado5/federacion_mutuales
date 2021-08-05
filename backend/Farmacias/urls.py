from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from  django.conf.urls.static import static

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'farmacias', views.FarmaciasViewSet, basename='farmacias')

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.listado_farmacias , name="Farmacias"),
    # path('listfarm/', views.listado_farmacias , name="Listado_Farm"),
    # path('altafarm/', views.alta_farmacia , name="Alta_Farm"),
    # path('modificarfarm/<int:cod_farmacia>/', views.modificar_farmacia , name="Modificar_Farm"),
    # path('actualizarfarm/<int:cod_farmacia>/', views.actualizar_farmacia , name="Actualizar_Farm"),
    # path('eliminarfarm/<int:cod_farmacia>/', views.eliminar_farmacia , name="Eliminar_Farm"),
    # path('listfarm/buscfarm/', views.buscar_farmacia , name="Buscar_Farm"),
]