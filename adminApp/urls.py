from django.urls import path
from adminApp.views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('my-profile/', profile, name='profile'),

    path('add-department/', addDepartment, name='addDepartment'),
    path('departments/', departments, name='departments'),
    path('departments/edit/<int:dept_id>/', editDepartment, name='editDepartment'),
    path('departments/delete/<int:dept_id>/', deleteDepartment, name='deleteDepartment'),

    path('designations/', designation_list, name='designation_list'),
    path('designations/add/', add_designation, name='add_designation'),
    path('designations/edit/<int:desig_id>/', edit_designation, name='edit_designation'),
    path('designations/delete/<int:desig_id>/', delete_designation, name='delete_designation'),

    path('add-employee/', addEmployee, name='addEmployee'),
    path('employeeList/', employeeList, name='employeeList'),
    path('employeeListView/', employeeListView, name='employeeListView'),

    path('holidays/', holiday_list, name='holiday_list'),
    path('holidays/add/', add_holiday, name='add_holiday'),
    path('holidays/edit/<int:holiday_id>/', edit_holiday, name='edit_holiday'),
    path('holidays/delete/<int:holiday_id>/', delete_holiday, name='delete_holiday'),
]