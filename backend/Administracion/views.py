from django.contrib.auth import authenticate, login, logout
from rest_framework import status , generics
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer


#Models
from  Administracion.models import CustomUser

class LoginView(APIView):
    serializer_class = UserSerializer
    #queryset = CustomUser.objects.all()

    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            _token, created = Token.objects.get_or_create(user=user)
            print(f"TOKEN : {_token}")
            if _token:
                login(request, user)
                return Response(_token.key ,status=status.HTTP_200_OK)
                #return Response(UserSerializer(user).data,status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(status=status.HTTP_404_NOT_FOUND)

    @classmethod
    def get_extra_actions(cls):
        return []
    

class LogoutView(APIView):
    #serializer_class = UserSerializer
    #queryset = CustomUser.objects.all()
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
    
    @classmethod
    def get_extra_actions(cls):
        return []


class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
    #queryset = CustomUser.objects.all()


    
    
    