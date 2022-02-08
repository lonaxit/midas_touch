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

class Loan(models.Model):
    # user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING,related_name='loan')
    active = models.BooleanField(default=True)
    transaction_code = models.BigIntegerField()
    applied_amount = models.DecimalField(max_digits=20,decimal_places=2)
    approved_amount = models.DecimalField(max_digits=20,decimal_places=2)
    monthly_deduction = models.DecimalField(max_digits=20,decimal_places=2)
    net_pay = models.DecimalField(max_digits=20,decimal_places=2)
    tenor = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(36)])
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    # review_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    
    # review_date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        
        return self.product.name + " loan"
    

class ConsolidatedLoan(models.Model):
    loan = models.ForeignKey(Loan,on_delete=models.CASCADE)
    credit = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    debit = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    transaction_code = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
# class Deduction(models.Model):
    
#     loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
#     credit= models.DecimalField(max_digits=20,decimal_places=2)
#     debit = models.DecimalField(max_digits=20,decimal_places=2)
#     balance = models.DecimalField(max_digits=20,decimal_places=2)
#     description = models.CharField(max_length=200)
#     deduction_month = models.DateField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
 

    
#     title= models.CharField(max_length=50)
#     storyline = models.CharField(max_length=200)
#     platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
#     active = models.BooleanField(default=True)
#     avg_rating = models.FloatField(default=0)
#     number_rating = models.IntegerField(default=0)
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title