from django.contrib import admin
from .models import cristales

# Register your models here.


class cristalesAdmin(admin.ModelAdmin):
    list_display = ("id_cristal","material","esfera","cilindro","eje","precio_laboratorio","precio_optica","precio_mutual","precio_venta","precio_tarjeta","stock")
    search_fields = ("id_cristal","material","esfera","cilindro","eje","precio_laboratorio","precio_optica","precio_mutual","precio_venta","precio_tarjeta","stock")
    ordering = ["id_cristal"]
    readonly_fields = ("created", "updated")


admin.site.register(cristales, cristalesAdmin)
