from django.db import models

class coinname(models.Model):
    name = models.CharField(max_length=100)
    hprice = models.FloatField(default=0)
    currprice= models.FloatField(default=0)
    rc = models.FloatField(default=0)

    def __str__(self):
        return self.name
