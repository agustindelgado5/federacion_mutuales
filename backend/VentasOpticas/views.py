from rest_framework import viewsets

from VentasOpticas.models import ventasOpticas
from Lentes.models import lentes
from django.db import transaction
from VentasOpticas.serializers import VentasOpticasSerializer

# Create your views here.


class VentasOpticasViewSet(viewsets.ModelViewSet):
    serializer_class = VentasOpticasSerializer
    queryset = ventasOpticas.objects.all()

    def create(self, request):       
        creado=super().create(request)
        data=creado.data
        venta=ventasOpticas.objects.filter(pk=data['id_venta']).first()
        venta.lente.stock-=1
        venta.cristal_derecho.stock-=1
        venta.cristal_izquierdo.stock-=1
        venta.lente.save()
        venta.cristal_izquierdo.save()
        venta.cristal_derecho.save()
        return creado

    def retrieve(self, request, pk=None):
        print("recibiendo") 
        return super().retrieve(request, pk=None)
    #     pass

    def update(self, request, pk=None):
        print("actualizando")
        ventaOLD=ventasOpticas.objects.filter(pk=pk).first()
        ventaOLD.lente.stock+=1
        ventaOLD.lente.save()
        ventaOLD.cristal_derecho.stock+=1
        ventaOLD.cristal_derecho.save()
        ventaOLD.cristal_izquierdo.stock+=1
        ventaOLD.cristal_izquierdo.save()
        updated=super().update(request, pk)
        venta=ventasOpticas.objects.filter(pk=pk).first()
        venta.lente.stock-=1
        venta.lente.save()
        venta.cristal_izquierdo.stock-=1
        venta.cristal_izquierdo.save()
        venta.cristal_derecho.stock-=1
        venta.cristal_derecho.save()
        return updated
    #     pass

    def partial_update(self, request, pk=None):
        print("actualizando parcial (borrado)")
        return super().partial_update(request, pk)
    #     pass

    def destroy(self, request, pk=None):
        print("Destroy")
        with transaction.atomic():
            ventaOLD=ventasOpticas.objects.filter(pk=pk).first()
            ventaOLD.lente.stock+=1
            ventaOLD.lente.save()
            ventaOLD.cristal_izquierdo.stock+=1
            ventaOLD.cristal_izquierdo.save()
            ventaOLD.cristal_derecho.stock+=1
            ventaOLD.cristal_derecho.save()
            deleted=super().destroy(request, pk=None)
            return deleted
        return 
    #     pass

# from django.shortcuts import render
