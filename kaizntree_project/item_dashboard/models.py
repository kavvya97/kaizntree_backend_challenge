from django.db import models

class Item(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    in_stock = models.IntegerField()
    available_stock = models.IntegerField()

    def __str__(self):
        return self.name
