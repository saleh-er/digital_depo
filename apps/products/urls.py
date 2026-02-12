from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('add/', views.product_create, name='product_create'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
]