from django.db import models
from shared.models.base import BaseModel
from .company import Company    

class Branch(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    address=models.TextField(blank=True, null=True)     
    status=models.BooleanField(default=True)
    phone = models.CharField(max_length=100, blank=True, null=True)   
    email = models.EmailField(blank=True, null=True)    
    def _str_(self):
        return f'{self.name}-{self.code}'    
   