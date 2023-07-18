from django.shortcuts import render
from .models import Employee, Role, Department
from .forms import AddEmployeeForm
from django.http import HttpResponse
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
            newEmp = Employee(first_name=form.cleaned_data['first_name'],
                              second_name=form.cleaned_data['second_name'],
                              dept=form.cleaned_data['dept'],
                              salary=form.cleaned_data['salary'],
                              bonus=form.cleaned_data['bonus'],
                              role=form.cleaned_data['role'],
                              phone=form.cleaned_data['phone'],
                              hire_date=form.cleaned_data['hire_date']
                              )
            newEmp.save()

            return HttpResponse('Employee Added Successfully')
    elif request.method == 'GET':
        form = AddEmployeeForm()
        context = {
            'form': form
        }
        print(form)
        return render(request, 'addEmp.html', context)


def removeEmp(request):
    return render(request, 'removeEmp.html')


def filterEmp(request):
    return render(request, 'filterEmp.html')
