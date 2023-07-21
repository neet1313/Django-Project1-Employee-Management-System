from django.shortcuts import render
from .models import Employee
from .forms import AddEmployeeForm, FilterEmployeeForm
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q

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
    if request.method == "POST":
        form = FilterEmployeeForm(request.POST)

        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name)
                               | Q(second_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name=dept)
        if role:
            emps = emps.filter(role__role=role)

        context = {
            'emps': emps
        }

        return render(request, 'allEmp.html', context)

    elif request.method == "GET":
        return render(request, 'filterEmp.html')
    else:
        return HttpResponse('There was an Error!')
