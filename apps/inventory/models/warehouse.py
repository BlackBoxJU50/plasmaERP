from django.db import models
from shared.models.base import BaseModel
from apps.core.models.branch import Branch

class Warehouse(BaseModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='warehouses')
    name = models.CharField(max_length=150)
    location = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
