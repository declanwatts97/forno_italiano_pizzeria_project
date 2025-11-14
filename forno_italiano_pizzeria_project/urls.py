"""
URL configuration for forno_italiano_pizzeria_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from forno_italiano_app import views as index_views
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    path('menu/', index_views.menu, name='menu'),
    path('our_restaurants/', index_views.our_restaurants, name='our_restaurants'),
    path('booking_form/', index_views.booking_form, name='booking_form'),
    path('', index_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('success/', index_views.booking_success, name='booking_success')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
