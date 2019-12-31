from django import forms
from bsh_user.models import WatchList


class Watchlist(forms.ModelForm):
    user = forms.Field()
    watchlist = forms.Field()

    price = forms.Field

    class Meta:
        model = WatchList
        fields = ('user', 'watchlist', 'price')
