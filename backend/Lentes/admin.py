from django.contrib import admin
from .models import lentes

# Register your models here.


class lentesAdmin(admin.ModelAdmin):
    list_display = ("codigo_optica","medida_lente", "patillas", "marca", "descripcion")
    search_fields = ("codigo_optica","medida_lente", "patillas", "marca", "descripcion")
    ordering = ["codigo_optica"]
    readonly_fields = ("created", "updated")


admin.site.register(lentes, lentesAdmin)
