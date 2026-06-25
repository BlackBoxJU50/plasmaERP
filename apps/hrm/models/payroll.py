from django.db import models
from shared.models.base import BaseModel
from .employee import Employee

class Payroll(BaseModel):
    PAID_STATUS_CHOICES = (
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid'),
        ('Processing', 'Processing'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payrolls')
    month = models.DateField(help_text="Select any date in the month for this payroll")
    basic_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    allowance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    bonus = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    deduction = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    paid_status = models.CharField(max_length=20, choices=PAID_STATUS_CHOICES, default='Unpaid')

    def __str__(self):
        return f"Payroll: {self.employee.first_name} - {self.month.strftime('%B %Y')}"
