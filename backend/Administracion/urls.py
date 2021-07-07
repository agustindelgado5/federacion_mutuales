from django.urls import path
from . import views
from django.conf import settings
from  django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.inicio , name="Administracion"),
    path('logout/', views.logout_page , name="Logout"),
    path('login/', views.login_page , name="Login"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 