from django.contrib import admin
from .models import Category, Unit, Product, Warehouse, Stock, StockMovement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'unit', 'cost_price', 'selling_price', 'status')
    search_fields = ('name', 'sku', 'barcode')
    list_filter = ('category', 'status')

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'location')
    list_filter = ('branch',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'quantity', 'reserved_qty', 'available_qty')
    list_filter = ('warehouse', 'product')

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'movement_type', 'quantity', 'movement_date')
    list_filter = ('movement_type', 'warehouse')
