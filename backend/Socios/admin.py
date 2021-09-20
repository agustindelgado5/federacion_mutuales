from django.contrib import admin

# from django.contrib.admin.sites import site
from .models import socios, familiar

# Register your models here.


class sociosAdmin(admin.ModelAdmin):
    list_display = ("numero_socio", "apellido", "nombre", "dni")
    search_fields = ("numero_socio", "apellido", "nombre", "dni")
    ordering = ["numero_socio"]
    # autocomplete_fields=['departamento']
    readonly_fields = ("edad", "created", "updated")


class familiaresAdmin(admin.ModelAdmin):
    list_display = ("dni_familiar", "apellido", "nombre", "numero_socio")
    search_fields = ("dni_familiar", "apellido", "nombre", "numero_socio")
    ordering = ["dni_familiar"]
    autocomplete_fields = ["numero_socio"]
    readonly_fields = ("edad", "created", "updated")


admin.site.register(socios, sociosAdmin)
admin.site.register(familiar, familiaresAdmin)
