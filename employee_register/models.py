from django.db import models

# Create your models here.

class Department(models.Model):
    DeptName = models.CharField(max_length=100)

    def __str__(self):
        return self.DeptName

class Employee(models.Model):
    EmpCode = models.CharField(max_length=5)
    EmpName = models.CharField(max_length=100)
    Salary = models.IntegerField()
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)