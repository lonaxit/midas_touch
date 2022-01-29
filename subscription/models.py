from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# importing User Model
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    about= models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory,on_delete=models.DO_NOTHING,related_name='product')
    
    def __str__(self):
        return self.name

# class Loan(models.Model):
    
#     title= models.CharField(max_length=50)
#     storyline = models.CharField(max_length=200)
#     platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
#     active = models.BooleanField(default=True)
#     avg_rating = models.FloatField(default=0)
#     number_rating = models.IntegerField(default=0)
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title