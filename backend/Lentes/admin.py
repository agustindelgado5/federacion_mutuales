from django.contrib import admin
from .models import lentes

# Register your models here.


class lentesAdmin(admin.ModelAdmin):
    list_display = ("id_lente","diametro_cristal","largo_patillas","ancho_puente","marca","color","material","descripcion","precio_optica","precio_mutual","precio_venta","precio_tarjeta","stock")
    search_fields = ("id_lente","diametro_cristal","largo_patillas","ancho_puente","marca","color","material","descripcion","precio_optica","precio_mutual","precio_venta","precio_tarjeta","stock")
    ordering = ["id_lente"]
    readonly_fields = ("created", "updated")


admin.site.register(lentes, lentesAdmin)
