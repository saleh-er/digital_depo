from django.shortcuts import render
from django.views.generic import ListView
# Change '.apps' to '.models'
from .models import Product
def home_temp(request):
    return render(request, 'home.html')