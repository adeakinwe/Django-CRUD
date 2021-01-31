from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def get_employees(request):
    context = {'get_employees':Employee.objects.all()}
    return render(request, 'employee_register/get_employees.html',context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html',{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def delete_employee(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
