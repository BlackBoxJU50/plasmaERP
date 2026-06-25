from django.db import models
from shared.models.base import BaseModel

class FiscalYear(BaseModel):
    year_name = models.CharField(max_length=50, unique=True)  
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True) 

    def __str__(self):
        return self.year_name
