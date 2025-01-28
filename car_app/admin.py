from django.contrib import admin
from .models import CarCategory, CarType, CarBrand, Car, CarCosiness, CarImage

# Unfold admin
from unfold.admin import ModelAdmin, TabularInline

# Inline configurations
class CarCosinessInline(TabularInline):
    model = CarCosiness
    extra = 1  # How many empty forms to display

class CarImageInline(TabularInline):
    model = CarImage
    extra = 1

# Main Car admin
@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_display = ('title', 'car_category', 'car_type', 'car_brand', 'transmission')
    list_filter = ('car_category', 'car_type', 'car_brand')
    search_fields = ('title', 'description')
    inlines = [CarCosinessInline, CarImageInline]

# Registering other models
@admin.register(CarCategory)
class CarCategoryAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

@admin.register(CarType)
class CarTypeAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

@admin.register(CarBrand)
class CarBrandAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

@admin.register(CarCosiness)
class CarCosinessAdmin(ModelAdmin):
    list_display = ('title',)

@admin.register(CarImage)
class CarImageAdmin(ModelAdmin):
    list_display = ('title', 'image')
