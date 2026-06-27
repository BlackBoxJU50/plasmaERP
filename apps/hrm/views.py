from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

@login_required(login_url='login')
def employee_list_view(request):
    employees = Employee.objects.all().order_by('-created_at')
    context={
        'employees':employees
    }
    return render(request, 'hrm/employee_list.html', context)

    
@login_required(login_url='login')
def employee_create_view(request): 

    if request.method == 'POST': 
        form = EmployeeForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('hrm:employee_list') 
    else: 
        form = EmployeeForm() 
    return render(request, 'hrm/employee_form.html', {'form': form}) 