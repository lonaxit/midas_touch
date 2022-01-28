from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# importing User Model
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    about= models.CharField(max_length=200)
    
    def __str__(self):
        return self.name