from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home/home.html',context)   

def fashionhub(request):
    context = {}
    return render(request, 'home/portfolio.html',context)   

def graphics(request):
    context = {}
    return render(request, 'home/graphics.html',context)   

def contact(request):
    context = {}
    return render(request, 'home/contact.html',context)   

def portfolio(request):
    context = {}
    return render(request, 'home/portfolioall.html',context)   

























"""
def sitemaps(request):
    context = {}
    return render(request, 'home/sitemap.xml',context)
"""