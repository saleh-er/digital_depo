from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# 1. La vue d'inscription (Celle que votre erreur réclame)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username} !')
            return redirect('login') # Assurez-vous d'avoir une route 'login'
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def home_temp(request):
    return render(request, 'home.html')