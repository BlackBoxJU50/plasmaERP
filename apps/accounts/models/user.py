from django.contrib.auth.models import AbstractUser
from django.db import models
from shared.models.base import BaseModel

class User(AbstractUser, BaseModel):
    employee_id = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'user'
        verbose_name = "User"
        verbose_name_plural = "Users"
