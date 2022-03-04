from django.contrib import admin
from .models import ventasOpticas

# Register your models here.


class ventasOpticasAdmin(admin.ModelAdmin):
    list_display = ("codigo_seguimiento")
    search_fields = ("codigo_seguimiento")
    ordering = ["codigo_seguimiento"]

    readonly_fields = ("created", "updated")


admin.site.register(ventasOpticas)
