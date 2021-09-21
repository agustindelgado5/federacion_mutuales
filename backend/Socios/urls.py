from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'socios', views.SociosViewSet, basename='socios')
router.register(r'aldia', views.SociosViewSet, basename='aldia')
router.register(r'familiar', views.FamiliarViewSet, basename='familiar')

urlpatterns = [
    path("", include(router.urls)),
    # path('', views.listado_socios , name="Socios"),
    #     path('inscripcion/', views.inscrib_socio , name="Inscripcion"),
    #     path('listsocios/', views.listado_socios , name="Listado"),
    #     path('listsociospdf/', views.listado_socios_pdf , name="PDF_Socios"),
    #     path('altasocios/', views.alta_socio , name="Alta"),
    #     path('modificarsocios/<int:numero_socio>/', views.modificar_socio , name="Modificar"),
    #     path('actualizarsocios/<int:numero_socio>/', views.actualizar_socio , name="Actualizar"),
    #     path('eliminarsocios/<int:numero_socio>/', views.eliminar_socio , name="Eliminar"),
    #     path('listsocios/buscsocios/', views.buscar_socio , name="Buscar"),
]
