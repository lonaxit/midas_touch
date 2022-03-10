# imports
# for use in ViewSet import get_object_or_404
from django.shortcuts import get_object_or_404
# import Response
from rest_framework.response import Response

# import validation errors
from rest_framework.exceptions import ValidationError

from rest_framework import status
# import models
from subscription.models import *

from subscription.api.serializers import *

# from rest_framework import mixins
from rest_framework import generics

# import here below used for class based views
from rest_framework.views import APIView

import pandas as pd
import openpyxl

import random
import string

from django.db.models import Q, Sum, Avg, Max, Min
from django.db import transaction


# test import
from rest_framework.parsers import MultiPartParser,FormParser


class ProductCategoryList(generics.ListCreateAPIView):
    # ListCreateAPIView gives us both the get and post methods
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    

class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # gives get, put and destroy methods
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

# products views
class ProductList(generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    # allow get, put and destroy methods
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsReviewUserOrReadOnly]
    
    # throttle_classes =[UserRateThrottle,AnonRateThrottle]
    
    # using ScopedRateThrottle
    # throttle_classes =[ScopedRateThrottle]
    # throttle_scope = 'review-detail'
    
class ProductByCategoryList(generics.ListAPIView):
    # ListCreateAPIView gives us both the get and post methods
    # queryset = Review.objects.all()
    serializer_class = ProductSerializer
    # adding permission, comment out since its a list or get request
    # permission_classes = [IsAuthenticated]
    
    # default throttle classes
    # throttle_classes =[UserRateThrottle, AnonRateThrottle]
    
    # throttle_classes =[ReviewListThrottle, AnonRateThrottle]
    
    # filtering backend
    # filter_backends = [DjangoFilterBackend]
    
    # pls mention the fields to be filtered against 
    # filterset_fields = ['review_user__username', 'active']
    
    # over writing default queryset 
    def get_queryset(self):
        # get the product category pk
        pk = self.kwargs['pk']
        return Product.objects.filter(category=pk)


# # list all loans available
# class LoanList(generics.ListCreateAPIView):
#     queryset = Loan.objects.all()
#     serializer_class = LoanSerializer

    
# # list all loans given a product id 
# class LoansByProduct(generics.ListAPIView):
  
#     serializer_class = LoanSerializer
  
    
#     # over writing default queryset 
#     def get_queryset(self):
#         # get the wachlist pk
#         pk = self.kwargs['pk']
#         return Loan.objects.filter(product=pk)
    

class LoanCreate(generics.CreateAPIView):
    
    serializer_class = LoanSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes=[ReviewCreateThrottle]
    
    def get_queryset(self):
        # just return the review object
        return Loan.objects.all()
     
    #  we need to overwrite the current function becos we need to pass the current movie ID for which review is being created
    
    def perform_create(self,serializer):
        
        # pk = self.kwargs.get('pk')
        # get movie
        # movie= WatchList.objects.get(pk=pk)
        
        # logic to prevent multiple creation of reviews by a user
        # review_user = self.request.user
        # review_queryset = Review.objects.filter(watchlist=movie,review_user=review_user)
        # if review_queryset.exists():
            
        #     raise ValidationError("You have already reviewed this watchlist")
        
        # # custom calculations
        # # check if rating is 0 
        # if movie.number_rating == 0:
        #     movie.avg_rating = serializer.validated_data['rating']
        # else:
        #     movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2
        
        # # increase the rating  
        # movie.number_rating = movie.number_rating + 1
        
        # # save
        # movie.save()
        
        # product = Product.objects.get(pk=serializer.validated_data['product'])
        # save together with related watchlist and user
        # serializer.save(product=product,review_user=review_user)
        serializer.save()

        
# class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
#       # allow get, put and destroy methods
#     queryset = Loan.objects.all()
#     serializer_class = LoanSerializer
#     # permission_classes = [IsReviewUserOrReadOnly]
    
#     # throttle_classes =[UserRateThrottle,AnonRateThrottle]
    
#     # using ScopedRateThrottle
#     # throttle_classes =[ScopedRateThrottle]
#     # throttle_scope = 'review-detail'


# class LoanUpload(generics.CreateAPIView):
#     serializer_class = LoanSerializer
#     parser_classes = (MultiPartParser, FormParser,)
    
#     def get_queryset(self):
#         # just return the review object
#         return Loan.objects.all()
    
#     def post(self, request, *args, **kwargs):
#         data = request.FILES['file']
#         reader = pd.read_excel(data)
#         dtframe = reader
        
#         with transaction.atomic():
#             # TODO
#             # 1 CREATE EACH LOAN IN THE LOAN MODEL
#             # 2. CREATE CORRESPONDING LOAN IN THE CONSOLIDATED LOANS TABLE AS DEBIT
            
#             print(dtframe.monthly_deduction.sum())

#             # TODO Save total sum of deductions in a summary table
            
#             # generate random number 
#             random_number = ''.join((random.choice(string.digits) for x in range(10)))
          
#             for dtframe in dtframe.itertuples():
                
                
#                 loanObj = Loan.objects.create(
#                                     product=Product.objects.get(pk=dtframe.product),
#                                     transaction_code = random_number,
#                                     applied_amount=dtframe.applied_amount,
#                                     approved_amount=dtframe.approved_amount,
#                                     monthly_deduction=dtframe.monthly_deduction,
#                                     net_pay=dtframe.net_pay,
#                                     tenor=dtframe.tenor
#                                     )
                                
                            
#         #     loanObj.save()
#         return Response(status=201)


# #create loan deductions
# class LoanDeductionCreate(generics.CreateAPIView):
    
#     serializer_class = LoanDeductionSerializer
#     # permission_classes = [IsAuthenticated]
#     # throttle_classes=[ReviewCreateThrottle]
    
#     def get_queryset(self):
        
#         return LoanDeduction.objects.all()
     
#     #  we need to overwrite the current function becos we need to pass the current movie ID for which review is being created
    
#     def perform_create(self,serializer):
        
#         # pk = self.kwargs.get('pk')
#         # get movie
#         # movie= WatchList.objects.get(pk=pk)
        
#         # logic to prevent multiple creation of reviews by a user
#         # review_user = self.request.user
#         # review_queryset = Review.objects.filter(watchlist=movie,review_user=review_user)
#         # if review_queryset.exists():
            
#         #     raise ValidationError("You have already reviewed this watchlist")
        
#         # # custom calculations
#         # # check if rating is 0 
#         # if movie.number_rating == 0:
#         #     movie.avg_rating = serializer.validated_data['rating']
#         # else:
#         #     movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2
        
#         # # increase the rating  
#         # movie.number_rating = movie.number_rating + 1
        
#         # # save
#         # movie.save()
        
#         # product = Product.objects.get(pk=serializer.validated_data['product'])
#         # save together with related watchlist and user
#         # serializer.save(product=product,review_user=review_user)
#         serializer.save()
    




      