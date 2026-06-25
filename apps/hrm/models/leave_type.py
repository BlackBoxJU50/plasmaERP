from django.db import models
from shared.models.base import BaseModel

class LeaveType(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    days_allowed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
