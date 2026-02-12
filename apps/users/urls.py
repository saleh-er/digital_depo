from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # Placeholder for a profile or dashboard
    path('profile/', views.profile, name='profile'),
    
    # Built-in Django Login/Logout (Highly recommended for GitHub projects)
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]