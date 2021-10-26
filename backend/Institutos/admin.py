from django.contrib import admin
from .models import institutos

# Register your models here.


class institutosAdmin(admin.ModelAdmin):
    list_display = ("codigo_institucion")
    search_fields = ("codigo_institucion")
    ordering = ["codigo_institucion"]
    readonly_fields = ("created", "updated")


admin.site.register(institutos)
