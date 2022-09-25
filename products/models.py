from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    profile = models.TextField(blank=True)
    photo   = models.ImageField(upload_to = 'seller/photos/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    photo   = models.ImageField(upload_to = 'product/photos/')

    def __str__(self):
        return self.name

