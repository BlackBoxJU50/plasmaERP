from django.db import models
from shared.models.base import BaseModel

class Permission(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True)
    module = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
