from django.db import models
from shared.models.base import BaseModel
from .purchase_order import PurchaseOrder
from apps.inventory.models.warehouse import Warehouse

class GoodsReceipt(BaseModel):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='goods_receipts')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='goods_receipts')
    received_date = models.DateField()
    received_by = models.CharField(max_length=150)

    def __str__(self):
        return f"GR for {self.purchase_order.po_number}"
