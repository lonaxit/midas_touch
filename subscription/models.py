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
    applied_amount = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    approved_amount = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    monthly_deduction = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    net_pay = models.DecimalField(max_digits=20,decimal_places=2)
    tenor = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(36)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        
        return self.product.name + " loan"
    

class ConsolidatedLoan(models.Model):
    # user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    loan = models.ForeignKey(Loan,on_delete=models.CASCADE,related_name='consolidatedloan')
    credit = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    debit = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    balance = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    transaction_date = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    narration = models.CharField(max_length=400)
    transaction_code = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
class Deduction(models.Model):
    
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE,related_name='deduction')
    credit= models.DecimalField(max_digits=20,decimal_places=2)
    debit = models.DecimalField(max_digits=20,decimal_places=2)
    balance = models.DecimalField(max_digits=20,decimal_places=2)
    description = models.CharField(max_length=200)
    transaction_code = models.BigIntegerField()
    transaction_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 

    
#     title= models.CharField(max_length=50)
#     storyline = models.CharField(max_length=200)
#     platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
#     active = models.BooleanField(default=True)
#     avg_rating = models.FloatField(default=0)
#     number_rating = models.IntegerField(default=0)
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title