from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=252)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)




class Offer(models.Model):
    offers = models.CharField(max_length=15)
    description = models.CharField(max_length=211)
    discount = models.FloatField()

