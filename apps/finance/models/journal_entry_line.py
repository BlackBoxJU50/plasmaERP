from django.db import models
from shared.models.base import BaseModel
from .journal_entry import JournalEntry
from .chart_of_accounts import ChartOfAccounts

class JournalEntryLine(BaseModel):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='lines')
    account = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE, related_name='journal_lines')
    debit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    credit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.journal_entry.voucher_no} - {self.account.account_name}"
