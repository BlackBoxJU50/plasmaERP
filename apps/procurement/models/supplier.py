from django.db import models
from shared.models.base import BaseModel

class Supplier(BaseModel):
    name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
