from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from  django.conf.urls.static import static

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'medicamentos', views.MedicamentosViewSet, basename='medicamentos')
router.register(r'recetas', views.RecetasViewSet, basename='recetas')

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.listado_medicamentos , name="Medicamentos"),
    # path('listmed/', views.listado_medicamentos , name="Listado_Medicam"),
    # path('altamed/', views.alta_medicamento , name="Alta_Medicam"),
    # path('modificarmed/<int:id_medicamento>/', views.modificar_medicamento , name="Modificar_Medicam"),
    # path('actualizarmed/<int:id_medicamento>/', views.actualizar_medicamento , name="Actualizar_Medicam"),
    # path('eliminarmed/<int:id_medicamento>/', views.eliminar_medicamento , name="Eliminar_Medicam"),
    # path('listmed/buscmed/', views.buscar_medicamento , name="Buscar_Medicam"),
]