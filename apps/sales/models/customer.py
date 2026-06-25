from django.db import models
from shared.models.base import BaseModel

class Customer(BaseModel):
    customer_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
