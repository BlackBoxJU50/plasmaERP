from django.db import models
from shared.models.base import BaseModel
from .product import Product
from .warehouse import Warehouse

class Stock(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stocks')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='stocks')
    quantity = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    reserved_qty = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    available_qty = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    class Meta:
        unique_together = ('product', 'warehouse')

    def __str__(self):
        return f"{self.product.name} - {self.warehouse.name}"
