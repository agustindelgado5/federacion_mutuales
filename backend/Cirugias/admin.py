from django.contrib import admin
from .models import cirugias

# Register your models here.


class cirugiasAdmin(admin.ModelAdmin):
    list_display = ("codigo_intervencion","descripcion", "nivel", "numero_ayudantes", "honorario_cirujano", "honorario_ayudante", "observacion")
    search_fields = ("descripcion", "nivel", "numero_ayudantes", "honorario_cirujano", "honorario_ayudante", "observacion")
    ordering = ["codigo_intervencion"]
    readonly_fields = ("created", "updated")


admin.site.register(cirugias, cirugiasAdmin)
