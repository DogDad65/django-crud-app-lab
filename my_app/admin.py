from django.contrib import admin
from .models import Bike, Category

# Register Bike and Category
@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'category')  # Show category in list view
    search_fields = ('brand', 'model', 'category__name')
    list_filter = ('category',)  # Filter by category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
