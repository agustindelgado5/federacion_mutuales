from django import forms
from django.contrib.auth.password_validation import password_changed
from django.contrib.messages.api import error
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,"Administracion/inicio.html")

def logout_page(request):
    logout(request)
    messages.info(request, 'Sesion cerrada')
    return redirect('Login')


def login_page(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            _usuario = form.cleaned_data.get('username')
            _contraseña = form.cleaned_data.get('password')
            user=authenticate(username=_usuario, password=_contraseña) 

            if user is not None:
                login(request, user)
                messages.info(request, 'Sesion iniciada')
                return redirect('Administracion')
            else:
                messages.error(request, 'El usuario o la contraseña son incorrectas')
        else:
            messages.error(request, 'El usuario o la contraseña son incorrectas')

    form=AuthenticationForm()

    return render(request,"Administracion/login.html", {"forms":form})
    
    