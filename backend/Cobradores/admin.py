from django.contrib import admin
from .models import cobradores

# Register your models here.


class cobradoresAdmin(admin.ModelAdmin):
    list_display = ("id_codigo", "apellido", "nombre")
    search_fields = ("id_codigo", "apellido", "nombre")
    ordering = ["id_codigo"]

    readonly_fields = ("created", "updated")


admin.site.register(cobradores)
