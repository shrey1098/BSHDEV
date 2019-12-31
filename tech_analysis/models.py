from django.db import models


class Conames(models.Model):
    Co_name = models.CharField(max_length=300)
    ticker = models.CharField(max_length=300)
    tick = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.Co_name
