from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'website', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'email', 'phone', 'address', 'website')
    ordering = ('name',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'email', 'phone', 'address')
    ordering = ('name',)

@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'description', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'code', 'description')
    ordering = ('name',)

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'symbol', 'exchange_rate', 'is_base', 'status')
    list_filter = ('is_base', 'status')
    search_fields = ('name', 'code', 'symbol')
    ordering = ('name',)    