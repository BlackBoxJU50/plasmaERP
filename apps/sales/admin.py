from django.contrib import admin
from .models import Customer, SalesOrder, SalesOrderItem, Delivery, Invoice, Payment

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer_code', 'phone', 'email', 'credit_limit')
    search_fields = ('name', 'customer_code', 'phone')

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer', 'order_date', 'total_amount', 'status')
    list_filter = ('status', 'order_date')

@admin.register(SalesOrderItem)
class SalesOrderItemAdmin(admin.ModelAdmin):
    list_display = ('sales_order', 'product', 'quantity', 'unit_price', 'subtotal')

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('sales_order', 'delivery_date', 'status')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer', 'sales_order', 'invoice_date', 'grand_total', 'status')
    list_filter = ('status', 'invoice_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'customer', 'amount', 'payment_method', 'payment_date')
