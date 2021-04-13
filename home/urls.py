from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [

    #path('sitemaps/', views.sitemaps, name='sitemaps'),
]


from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from .views import (
    FashionsListView,
    GraphicsListView,
    FashionDetailView,
    GraphicDetailView,
    GraphicsSearchListView,
    FashionsSearchListView,
)
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('braams-graphics',GraphicsListView.as_view(), name="graphics"),
    path('contact/', views.contact, name='contact'),
    #path('checkout/', views.checkout, name="checkout"),
    #path('update_item/', views.updateItem, name="update_item"),
    #path('cart/', views.cart, name="cart"),
    path('braams-fashion-hub', FashionsListView.as_view(), name='fashionhub'),
    path('fashion/<slug:slug>/', FashionDetailView.as_view(), name='fashion-detail'),
    path('graphics/<slug:slug>/', GraphicDetailView.as_view(), name='graphic-detail'),
 
    path('search-graphics/',GraphicsSearchListView.as_view(), name="graphics_search_list_view"),
    path('search-fashion-hub/',FashionsSearchListView.as_view(), name="fashions_search_list_view"),
]
