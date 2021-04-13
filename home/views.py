from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
import json
from django.urls import  reverse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin
from django.db.models import Count
from django.contrib import messages
from django.forms import modelformset_factory
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
) 
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
import operator
from django.core import serializers
from functools import reduce
from django.db.models import Q

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home/home.html',context)   

def contact(request):
    context = {}
    return render(request, 'home/contact.html',context)  

class GraphicsListView(ListView):
    model = Graphic
    template_name = 'home/graphics.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'graphics'
    #ordering = ['-last_rating']
    paginate_by = 6
    
class FashionsListView(ListView):
    model = Fashion
    template_name = 'home/fashion.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'fashions'
    #ordering = ['-last_rating']
    paginate_by = 6

class GraphicDetailView(DetailView):
    model = Graphic
    template_name = 'home/graphic_detailpage.html'
    def get_success_url(self):
        return reverse('graphic-detail', kwargs={'slug': self.object.slug})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FashionDetailView(DetailView):
    model = Fashion
    template_name = 'home/fashion_detailpage.html'
    def get_success_url(self):
        return reverse('fashion-detail', kwargs={'slug': self.object.slug})

def search(request):
    context = {
        'graphics': Graphic.objects.filter(title__contains=request.GET['title'])
    }
    
    return render(request, 'home/graphics_search_results.html', context)

def search(request):
    context = {
        'fashions': Fashion.objects.filter(title__contains=request.GET['title'])
    }
    
    return render(request, 'home/fashions_search_results.html', context)


class GraphicsSearchListView(GraphicsListView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 6

    def get_queryset(self):
        result = super(GraphicsSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(overview__icontains=q) for q in query_list))
            )

        return result
    
class FashionsSearchListView(FashionsListView):
    """
        Display a Blog List page filtered by the search query.
    """
    paginate_by = 6

    def get_queryset(self):
        result = super(FashionsSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
            reduce(operator.and_,
                    (Q(title__icontains=q) for q in query_list)) |
            reduce(operator.and_,
                    (Q(overview__icontains=q) for q in query_list))
            )

        return result


"""
def sitemaps(request):
    context = {}
    return render(request, 'home/sitemap.xml',context)
"""