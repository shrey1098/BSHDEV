from django.db import models

class Homepage_db(models.Model,):
    hco_name = models.CharField(max_length=300, default='')
    htic_name = models.CharField(max_length=300, default='')
    hco_logo = models.ImageField(default='')

    def __str__(self):
        return self.hco_name
