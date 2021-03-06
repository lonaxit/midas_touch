from unicodedata import category
from rest_framework import serializers
# import models
from subscription.models import *


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
     

# class LoanDeductionSerializer(serializers.ModelSerializer):

#     # serializer relations
#     loandeduction_user = serializers.StringRelatedField(read_only=True)
    
#     class Meta:
#         model= LoanDeduction
    
#         fields= "__all__"



class LoanSerializer(serializers.ModelSerializer):
    loan_user = serializers.StringRelatedField(read_only=True)

    # describing relationships
    
    # deductions = LoanDeductionSerializer(many=True,read_only=True)
    product = ProductSerializer(many=True,read_only=True) 
    # product = ProductSerializer(many=True,required=True)
    

    # file = serializers.FileField()
    
    class Meta:
        model= Loan
        fields = '__all__'

        

# class ConsolidatedLoanSerializer(serializers.ModelSerializer):

#     consolidatedloan_user = serializers.StringRelatedField(read_only=True)
    
#     class Meta:
#         model=  ConsolidatedLoan
    
#         fields= "__all__"
        


# class LoanDeductionSummary(serializers.ModelSerializer):
    
#     class Meta:
#         model = LoanDeductionSummary
        
#         fields= "__all__"