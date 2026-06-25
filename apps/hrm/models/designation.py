from django.db import models
from shared.models.base import BaseModel
from .department import Department

class Designation(BaseModel):
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='designations')

    def __str__(self):
        return f"{self.name} - {self.department.name}"
