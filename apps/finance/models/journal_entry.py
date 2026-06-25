from django.db import models
from shared.models.base import BaseModel
from apps.accounts.models.user import User

class JournalEntry(BaseModel):
    voucher_no = models.CharField(max_length=50, unique=True)
    entry_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='journal_entries')

    def __str__(self):
        return self.voucher_no
