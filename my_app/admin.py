from django.contrib import admin
from .models import Bike, Category, Maintenance, Upgrade

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'category')
    search_fields = ('brand', 'model', 'category__name')
    list_filter = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('bike', 'maintenance_type', 'date')
    search_fields = ('bike__brand', 'maintenance_type')
    list_filter = ('maintenance_type', 'date')

@admin.register(Upgrade)
class UpgradeAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'date_installed', 'bike')
    search_fields = ('type', 'description')
    list_filter = ('type', 'date_installed')
