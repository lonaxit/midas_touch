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
    
    
    # loan endpoints
    path('loans/',LoanList.as_view(),name='loans'),
    path('loan-create/',LoanCreate.as_view(),name='loan-create'),
    
    path('<int:pk>/loans/', LoansByProduct.as_view(), name="product-loans"),
    path('loan/<int:pk>/', LoanDetail.as_view(),name='loan-detail'),
     path('loan/upload/', LoanUpload.as_view(),name='loan-upload'),
     
    # path('<int:pk>/', WatchDetailAV.as_view(), name="movie-detail"),
    
     # get reviews for a particular watchlist
    # path('<int:pk>/reviews/', ReviewList.as_view(), name="review-list"),
    
    # to test filters on watch list
    # path('list2/',WatchListGV.as_view(), name='list2'),
    
]