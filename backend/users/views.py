from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

# from django.contrib.auth.models import User
from users.models import User


@api_view(["GET"])
def login(request):
    user = User.objects.get(username="admin")

    token = Token.objects.create(user=user)
