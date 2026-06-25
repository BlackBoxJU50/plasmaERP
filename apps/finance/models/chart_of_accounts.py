from django.db import models
from shared.models.base import BaseModel

class ChartOfAccounts(BaseModel):
    TYPE_CHOICES = (
        ('Asset', 'Asset'),
        ('Liability', 'Liability'),
        ('Equity', 'Equity'),
        ('Revenue', 'Revenue'),
        ('Expense', 'Expense'),
    )

    account_code = models.CharField(max_length=50, unique=True)
    account_name = models.CharField(max_length=150)
    account_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    parent_account = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_accounts')

    def __str__(self):
        return f"{self.account_code} - {self.account_name}"
