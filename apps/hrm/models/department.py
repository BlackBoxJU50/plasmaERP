from django.db import models
from shared.models.base import BaseModel

class Department(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
