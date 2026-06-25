from django.db import models
from shared.models.base import BaseModel
from .supplier import Supplier

class PurchaseOrder(BaseModel):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Confirmed', 'Confirmed'),
        ('Received', 'Received'),
        ('Cancelled', 'Cancelled'),
    )

    po_number = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateField()
    expected_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return self.po_number
