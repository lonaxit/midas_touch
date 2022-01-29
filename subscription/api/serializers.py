from rest_framework import serializers
# import models
from subscription.models import *



class ProductCategorySerializer(serializers.ModelSerializer):
    # control what is returned in our nested relationship 
    # review_user = serializers.StringRelatedField(read_only=True)
    
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
    
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Product
    
        fields= "__all__"
     
    