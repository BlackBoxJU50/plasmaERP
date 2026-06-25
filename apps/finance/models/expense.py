from django.db import models
from shared.models.base import BaseModel
from .chart_of_accounts import ChartOfAccounts

class Expense(BaseModel):
    expense_type = models.CharField(max_length=150)
    account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    expense_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.expense_type} - {self.amount}"
