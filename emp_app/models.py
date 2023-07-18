from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"name - {self.name} location - {self.location}"


class Role(models.Model):
    role = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"role - {self.role}"


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    second_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
