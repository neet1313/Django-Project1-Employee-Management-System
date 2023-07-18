from django.contrib import admin
from .models import Role, Employee, Department

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "salary",
                    "bonus", "phone", "hire_date")


class RoleAdmin(admin.ModelAdmin):
    list_display = ("role")


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "location")


admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
