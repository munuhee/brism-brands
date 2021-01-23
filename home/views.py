from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home/home.html',context)   
"""
def sitemaps(request):
    context = {}
    return render(request, 'home/sitemap.xml',context)
"""