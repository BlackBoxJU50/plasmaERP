from django.contrib import admin
from .models import ApprovalFlow

@admin.register(ApprovalFlow)
class ApprovalFlowAdmin(admin.ModelAdmin):
    list_display = ('name', 'module')
