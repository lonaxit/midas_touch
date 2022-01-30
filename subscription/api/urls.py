from django.urls import path,include
from subscription.api.views import *



urlpatterns = [

    # product category endpoints
    path('product-category/',ProductCategoryList.as_view(), name='product-category'),
    
     path('productcategory/<int:pk>/',ProductCategoryDetail.as_view(), name='productcategory-detail'),
     
    #  products endpoints
    path('products/',ProductList.as_view(), name='products'),
    
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    
    path('<int:pk>/products/', ProductByCategoryList.as_view(), name="product-list"),
     
    # path('<int:pk>/', WatchDetailAV.as_view(), name="movie-detail"),
    
     # get reviews for a particular watchlist
    # path('<int:pk>/reviews/', ReviewList.as_view(), name="review-list"),
    
    # to test filters on watch list
    # path('list2/',WatchListGV.as_view(), name='list2'),
    
]