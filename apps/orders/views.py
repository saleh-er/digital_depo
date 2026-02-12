from django.shortcuts import render

# Une vue simple pour plus tard
def cart_detail(request):
    return render(request, 'orders/cart.html')