from django.db import models
from shared.models.base import BaseModel
from .chart_of_accounts import ChartOfAccounts

class Revenue(BaseModel):
    source = models.CharField(max_length=150)
    account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, related_name='revenues')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.source} - {self.amount}"
