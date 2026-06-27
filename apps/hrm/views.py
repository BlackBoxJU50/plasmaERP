from django.shortcuts import get_object_or_404
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

@login_required(login_url='login')
def employee_edit_view(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('hrm:employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'hrm/employee_form.html', {'form': form})

@login_required(login_url='login')
def employee_delete_view(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('hrm:employee_list')
    return render(request, 'hrm/employee_confirm_delete.html', {'employee': employee})




    
        
    