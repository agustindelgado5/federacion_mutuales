from django.contrib import admin
from .models import servicios

# Register your models here.


class serviciosAdmin(admin.ModelAdmin):
    list_display = ("id_servicio", "nombre")
    search_fields = ("id_servicio", "nombre")
    ordering = ["id_servicio"]
    readonly_fields = ("created", "updated")


admin.site.register(servicios)
