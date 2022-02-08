from unicodedata import category
from rest_framework import serializers
# import models
from subscription.models import *


class LoanSerializer(serializers.ModelSerializer):
    # product = serializers.StringRelatedField(read_only=True)
    
    # product = ProductSerializer(many=True,read_only=True) 
    file = serializers.FileField()
    
    class Meta:
        model= Loan
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    
    # This is to enable the related field appear as a string rather than its id or pk
    # category = serializers.CharField(source='category.name')
    
    # loan = LoanSerializer(many=True,read_only=True)
    
    
    class Meta:
        model= Product
    
        fields= "__all__"
        
        
class ProductCategorySerializer(serializers.ModelSerializer):
    
    # nested relationships --- displays all products related to this product category
    product = ProductSerializer(many=True,read_only=True) 
    
    class Meta:
        model= ProductCategory
    
        fields= "__all__"
        
    
    # field validators
    # def validate_name(self,value):
    #     if len(value) == 1:
    #         raise serializers.ValidationError("Empty name is not allowed!")
    #     return value
    # def validate_about(self,value):
        
    #     if len(value) == 1: 
    #         raise serializers.ValidationError("Enter a description")
    #     return value
     
    
