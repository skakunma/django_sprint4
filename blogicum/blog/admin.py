from django.contrib import admin
from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_published', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['is_published', 'created_at']


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published', 'created_at']
    search_fields = ['name']
    list_filter = ['is_published', 'created_at']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category',
                    'location', 'pub_date', 'is_published', 'created_at']
    search_fields = ['title', 'text', 'author__username']
    list_filter = ['pub_date', 'author', 'category', 'location',
                   'is_published', 'created_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
