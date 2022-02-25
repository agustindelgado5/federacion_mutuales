from django.contrib import admin
from .models import estudios

# Register your models here.


class estudiosAdmin(admin.ModelAdmin):
    list_display = ("id_estudio","tipo",  "abreviatura", "ub",  "descripcion", "denominación")
    search_fields = ("tipo", "abreviatura", "ub", "descripcion", "denominación")
    ordering = ["id_estudio"]
    readonly_fields = ("created", "updated")


admin.site.register(estudios, estudiosAdmin)
