from django.db import models
from shared.models.base import BaseModel
from .department import Department
from .designation import Designation
from apps.core.models.branch import Branch

class Employee(BaseModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    employee_code = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    joining_date = models.DateField()
    
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, related_name='employees')
    
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.BooleanField(default=True, help_text="Is the employee currently active?")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_code})"
