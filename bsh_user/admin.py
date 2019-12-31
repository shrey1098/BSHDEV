from django.contrib import admin
from bsh_user.models import WatchList


class WatchListAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user", "watchlist", "price", "signal",)


admin.site.register(WatchList, WatchListAdmin)
