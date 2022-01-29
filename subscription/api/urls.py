from django.urls import path,include
from subscription.api.views import *



urlpatterns = [

    # list and create
    path('product-category/',ProductCategoryList.as_view(), name='product-category'),
    
    # product category detail
     path('productcategory/<int:pk>/',ProductCategoryDetail.as_view(), name='productcategory-detail'),
     
    # path('<int:pk>/', WatchDetailAV.as_view(), name="movie-detail"),
    
    # to test filters on watch list
    # path('list2/',WatchListGV.as_view(), name='list2'),
    
]