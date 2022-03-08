from django.contrib import admin
from .models import ventasOpticas

# Register your models here.


class ventasOpticasAdmin(admin.ModelAdmin):
    list_display = ("id_venta","numero_socio","lente","cristal_derecho","cristal_izquierdo","fecha_receta","fecha_venta")
    search_fields = ("id_venta","numero_socio","lente","cristal_derecho","cristal_izquierdo","fecha_receta","fecha_venta")
    ordering = ["id_venta"]

    readonly_fields = ("created", "updated")


admin.site.register(ventasOpticas)
