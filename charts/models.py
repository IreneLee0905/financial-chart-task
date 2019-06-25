from django.db import models


# Create your models here.


class Stock(models.Model):
    data = models.FloatField(default=0)
    date = models.DateField()

    def save(self, *args, **kwargs):
        super(Stock, self).save(*args, **kwargs)