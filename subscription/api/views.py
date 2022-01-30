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