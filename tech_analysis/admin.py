from django.contrib import admin
from .models import Conames


class ConamesAdmin(admin.ModelAdmin):
    list_display = ("Co_name", "ticker",)


admin.site.register(Conames, ConamesAdmin)
