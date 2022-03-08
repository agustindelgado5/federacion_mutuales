from django.contrib import admin

from .models import vendedores

# Register your models here.


class vendedoresAdmin(admin.ModelAdmin):
    list_display = ("id_vendedor", "apellido", "nombre")
    search_fields = ("id_vendedor", "apellido", "nombre")
    ordering = ["id_vendedor"]

    readonly_fields = ("created", "updated")

admin.site.register(vendedores)