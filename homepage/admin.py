from django.contrib import admin
from homepage.models import Homepage_db


class homepage_dbAdmin(admin.ModelAdmin):
    list_display = ("hco_name", "htic_name", "hco_logo")


admin.site.register(Homepage_db, homepage_dbAdmin)