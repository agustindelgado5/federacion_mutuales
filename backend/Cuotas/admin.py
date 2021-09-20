from django.contrib import admin

from .models import cuotas

# Register your models here.


class cuotasAdmin(admin.ModelAdmin):
    list_display = ("id_cuota", "personapago", "monto", "fecharealizacion")
    search_fields = ("id_cuota", "personapago", "monto", "fecharealizacion")
    ordering = ["id_cuota"]
    readonly_fields = ("created", "updated")


admin.site.register(cuotas, cuotasAdmin)
