from django.db import models
from shared.models.base import BaseModel
from .goods_receipt import GoodsReceipt
from apps.inventory.models.product import Product

class GoodsReceiptItem(BaseModel):
    goods_receipt = models.ForeignKey(GoodsReceipt, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gr_items')
    received_qty = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"GR Item: {self.product.name}"
