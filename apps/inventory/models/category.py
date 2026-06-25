from django.db import models
from shared.models.base import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name
