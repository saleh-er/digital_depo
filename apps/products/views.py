from django.shortcuts import render
from django.views.generic import ListView
# Change this line:
from apps.products.apps import Product 

def home_temp(request):
    return render(request, 'home.html')