from django.db import models
from shared.models.base import BaseModel

class CostCenter(BaseModel):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
