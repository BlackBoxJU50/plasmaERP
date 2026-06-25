from django.db import models
from shared.models.base import BaseModel
from .sales_order import SalesOrder

class Delivery(BaseModel):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='deliveries')
    delivery_date = models.DateField()
    status = models.CharField(max_length=50, default='Processing')

    def __str__(self):
        return f"Delivery for {self.sales_order.order_number}"
