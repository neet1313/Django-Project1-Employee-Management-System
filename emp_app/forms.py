from django import forms
from .models import Employee


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        labels = {
            "first_name": "First Name",
            "second_name": "Last Name",
            "dept": "Department",
            "hire_date": "Hire Date"
        }


class FilterEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'second_name', 'dept', 'role']
        labels = {
            "first_name": "First Name",
            "second_name": "Last Name",
            "dept": "Department"
        }
