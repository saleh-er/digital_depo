from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Routing to our modular apps
    path('', include('apps.products.urls')),
    path('users/', include('apps.users.urls')),
    path('orders/', include('apps.orders.urls')),
]

# This serves your uploaded media files (thumbnails, digital downloads) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)