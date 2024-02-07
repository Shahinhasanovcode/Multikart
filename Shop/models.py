from django.db import models

# Create your models here.
class Collection(models.Model):
    brand = models.CharField(max_length=50 )
    colors =models.CharField()
    size = models.CharField(max_length=50)
    price = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shop(models.Model):
    image = models.ImageField(upload_to='media/Shop')   
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
