from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('braams-fashion-hub/', views.fashionhub, name='fashionhub'),
    path('braams-graphics/', views.graphics, name='graphics'),
    path('contact/', views.contact, name='contact'),
     path('portfolio/', views.portfolio, name='portfolio'),
    #path('sitemaps/', views.sitemaps, name='sitemaps'),
]
