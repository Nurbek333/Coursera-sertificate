from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    path('', include('home.urls')),  # Change to ads.urls
    path('admin/', admin.site.urls),  # Keep
    path('accounts/', include('django.contrib.auth.urls')),  # Keep

    # Sample applications
    path('autos/', include('autos.urls')),
]
