from django.contrib import admin
from .models import ChartOfAccounts, JournalEntry, JournalEntryLine, Expense, Revenue

@admin.register(ChartOfAccounts)
class ChartOfAccountsAdmin(admin.ModelAdmin):
    list_display = ('account_code', 'account_name', 'account_type', 'parent_account')
    list_filter = ('account_type',)
    search_fields = ('account_code', 'account_name')

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('voucher_no', 'entry_date', 'created_by')
    search_fields = ('voucher_no',)

@admin.register(JournalEntryLine)
class JournalEntryLineAdmin(admin.ModelAdmin):
    list_display = ('journal_entry', 'account', 'debit', 'credit')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_type', 'account', 'amount', 'expense_date')
    list_filter = ('expense_date',)

@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ('source', 'account', 'amount', 'date')
    list_filter = ('date',)
