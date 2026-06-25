from django.db import models
from shared.models.base import BaseModel

class Unit(BaseModel):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.symbol})"
