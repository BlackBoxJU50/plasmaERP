from django.contrib import admin
from .models import Supplier, PurchaseOrder, PurchaseOrderItem, GoodsReceipt, GoodsReceiptItem

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'email')
    search_fields = ('name', 'phone')

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'supplier', 'order_date', 'expected_date', 'total_amount', 'status')
    list_filter = ('status', 'order_date')

@admin.register(PurchaseOrderItem)
class PurchaseOrderItemAdmin(admin.ModelAdmin):
    list_display = ('purchase_order', 'product', 'quantity', 'unit_price', 'subtotal')

@admin.register(GoodsReceipt)
class GoodsReceiptAdmin(admin.ModelAdmin):
    list_display = ('purchase_order', 'warehouse', 'received_date', 'received_by')

@admin.register(GoodsReceiptItem)
class GoodsReceiptItemAdmin(admin.ModelAdmin):
    list_display = ('goods_receipt', 'product', 'received_qty')
