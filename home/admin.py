from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Fashion)
class FashionAdmin(admin.ModelAdmin):
    fields = ('title', 'overview', 'description','cover_image', 'photo_one', 'photo_two', 'photo_three', 'photo_four')

    list_display = ('title', 'overview', 'description','cover_image', 'slug')
    search_fields = ['title']
  
@admin.register(Graphic)    
class GraphicAdmin(admin.ModelAdmin):
    fields = ('title', 'overview', 'description','cover_image', 'photo_one', 'photo_two')

    list_display = ('title', 'overview', 'description','cover_image', 'slug')
    search_fields = ['title']