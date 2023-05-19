from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    def __str__(self):
        return self.name
    
# class Offer(models.Model):
#     code = models.CharField(max_length=12)
#     description = models.CharField(max_length=2300)
#     discount = models.FloatField()   

class NewArrival(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)
    product_id = models.CharField(max_length=255)
    arrival_date = models.DateField()
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    brand = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    # def __str__(self):
    #     return self.name

        