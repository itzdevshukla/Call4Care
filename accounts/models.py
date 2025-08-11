from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock_field = models.CharField(max_length=100)
