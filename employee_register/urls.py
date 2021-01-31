from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('list/', views.get_employees, name='get_employees'),
    path('delete/<int:id>', views.delete_employee, name='delete_employee')
]