from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Ordenes.models import ordenes
from Ordenes.serializers import OrdenesSerializer

# Create your views here.


class OrdenesViewSet(viewsets.ModelViewSet):
    serializer_class = OrdenesSerializer
    queryset = ordenes.objects.all()
    @action(methods=['GET'], detail = True)
    def declararOrden(self, request, pk=None):
        print("escribiendo en viewset ")
        o =self.get_object()
        token=int(request.query_params["token"])
        mje=o.verificarOrden(token)
        return Response({"Verificacion": mje})
