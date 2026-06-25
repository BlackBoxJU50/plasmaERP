from django.db import models
from shared.models.base import BaseModel
class Currency(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=5)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    is_base = models.BooleanField(default=False)
    status= models.BooleanField(default=True)


    def __str__(self):
        return f"{self.code}"