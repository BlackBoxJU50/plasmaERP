from django.db import models
from shared.models.base import BaseModel
from .invoice import Invoice
from .customer import Customer

class Payment(BaseModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_date = models.DateField()
    reference_no = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Payment {self.amount} for {self.invoice.invoice_number}"
