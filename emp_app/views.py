from django.shortcuts import render
from .models import Employee, Role, Department
from .forms import AddEmployeeForm
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'index.html')


def allEmp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'allEmp.html', context)


def addEmp(request):
    if request.method == "POST":
        form = AddEmployeeForm(request.POST)

        if form.is_valid():
            first_name = request.POST['first_name']
            second_name = request.POST['second_name']
            dept = request.POST['dept']
            salary = int(request.POST['salary'])
            bonus = int(request.POST['bonus'])
            role = int(request.POST['role'])
            phone = int(request.POST['phone'])

            newEmp = Employee(first_name=first_name, second_name=second_name, dept_id=dept,
                              salary=salary, bonus=bonus, role_id=role, phone=phone, hire_date=datetime.now())
            newEmp.save()

            return HttpResponse('Employee Added Successfully')
    elif request.method == 'GET':
        form = AddEmployeeForm()
        context = {
            'form': form
        }
        print(form)
        return render(request, 'addEmp.html', context)
    else:
        return HttpResponse('An Exception Occured while adding the employee!')


def removeEmp(request, emp_id=0):
    if emp_id:
        try:
            removeEmp = Employee.objects.get(id=emp_id)
            removeEmp.delete()
            return HttpResponse('Employee Successfully Deleted!')
        except:
            return HttpResponse('An Error occured while deleting')

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'removeEmp.html', context)


def filterEmp(request):
    return render(request, 'filterEmp.html')
