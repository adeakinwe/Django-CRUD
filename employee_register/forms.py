from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
      model = Employee   
      fields = ('EmpCode','EmpName','Salary','Department')
      labels = {
          'EmpName': 'Full Name',
          'EmpCode': 'Staff Code'
      }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['Department'].empty_label = "Select Department"
        self.fields['EmpCode'].required = False