from django.db import models
from shared.models.base import BaseModel

class ApprovalFlow(BaseModel):
    name = models.CharField(max_length=150)
    module = models.CharField(max_length=50)

    def __str__(self):
        return self.name
