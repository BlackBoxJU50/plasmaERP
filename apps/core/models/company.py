from django.db import models
from shared.models.base import BaseModel

class Company(BaseModel):
    name = models.CharField(max_length=100)
    trade_license= models.CharField(max_length=100, blank=True, null=True)
    tin = models.CharField(max_length=100, blank=True, null=True)     
    email = models.EmailField(blank=True, null=True)     
    phone = models.CharField(max_length=100, blank=True, null=True)   
    address = models.TextField(blank=True, null=True) 
    website= models.URLField(blank=True, null=True)    
    status=models.BooleanField(default=True)
    
    