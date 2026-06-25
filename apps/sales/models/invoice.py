from django.db import models
from shared.models.base import BaseModel
from .sales_order import SalesOrder
from .customer import Customer

class Invoice(BaseModel):
    invoice_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='invoices')
    invoice_date = models.DateField()
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    status = models.CharField(max_length=50, default='Unpaid')

    def __str__(self):
        return self.invoice_number
