"""real_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from listings.views import listing_list, listing_retrieve, listing_create, listing_update, listing_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', listing_list, name='listing_list'),  # Name added for the listing view
    path('listings/<pk>/', listing_retrieve, name='listing_detail'),  # Updated name for listing details
    path('add-listing/', listing_create, name='listing_create'),
    path('listings/<pk>/edit/', listing_update, name='listing_update'),
    path('listings/<pk>/delete/', listing_delete, name='listing_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
