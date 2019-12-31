from django.db import models
from django.contrib.auth.models import User


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watchlist = models.CharField(max_length=300, default='Explore Stocks and Add them to your watchlist')
    price = models.FloatField(default='')
    signal = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.watchlist
