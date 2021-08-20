from django.contrib import admin
from .models import farmacias

# Register your models here.


class farmaciasAdmin(admin.ModelAdmin):
    list_display = ("cod_farmacia", "matricula_farm", "farmacia")
    search_fields = ("cod_farmacia", "matricula_farm", "farmacia")
    ordering = ["cod_farmacia"]
    # autocomplete_fields=['departamento']
    readonly_fields = ("created", "updated")


admin.site.register(farmacias)
