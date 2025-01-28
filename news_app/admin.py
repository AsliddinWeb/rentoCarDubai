from django.contrib import admin
from .models import Category, NewsImage, News

# Unfold admin
from unfold.admin import ModelAdmin

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(NewsImage)
class NewsImageAdmin(ModelAdmin):
    list_display = ('id', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id',)

@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('title', 'body')
    autocomplete_fields = ('category',)
    filter_horizontal = ('images',)
