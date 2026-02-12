from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
# Note: Tu devras créer un fichier forms.py si tu veux utiliser ProductForm
# from .forms import ProductForm 

def product_list(request):
    """Affiche tous les produits disponibles"""
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    """Affiche les détails d'un produit spécifique"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def product_create(request):
    """Permet à un utilisateur connecté de poster un produit"""
    if request.method == "POST":
        # Logique simplifiée sans ProductForm pour l'exemple
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            image=image,
            seller=request.user
        )
        return redirect('products:product_list')
        
    return render(request, 'products/product_form.html')

@login_required
def product_delete(request, pk):
    """Supprime un produit si l'utilisateur est le vendeur"""
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.seller:
        product.delete()
    return redirect('products:product_list')