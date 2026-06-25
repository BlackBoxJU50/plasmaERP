from django.db import models
from shared.models.base import BaseModel
from apps.accounts.models.user import User

class AuditLog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.action} on {self.model_name}"
