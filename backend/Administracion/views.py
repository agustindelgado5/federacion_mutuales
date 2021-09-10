from django.contrib.auth import authenticate, login, logout
from rest_framework import status , generics
from rest_framework import mixins, viewsets
from rest_framework.response import Response
#from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password

#Models
from  Administracion.models import CustomUser

class LoginView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            #return Response(status=status.HTTP_200_OK)
            return Response(UserSerializer(user).data,status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def validate_password(self, value):
        return make_password(value)
    
      

class LogoutView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

    


class SignupView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    #serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def validate_password(self, value):
        return make_password(value)
    
    