from rest_framework import serializers
#from django.contrib.auth import get_user_model
from .models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        #model = get_user_model()
        model = CustomUser
        fields = ('email', 'username', 'password')