from django.urls import path
from base.views import product_views as views


urlpatterns = [

    path('', views.getProducts, name="products"),
    path('create/', views.createProduct, name="product-create"),
    path('upload/', views.upload_image, name="image-upload"),
    path('<str:pk>/', views.getProduct, name="product"),
    path('update/<str:pk>/', views.update_product, name="product-update"),
    path('delete/<str:pk>/', views.deleteProduct, name="product-delete"),

]
