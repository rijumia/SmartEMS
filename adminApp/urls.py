from django.urls import path
from adminApp.views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('my-profile/', profile, name='profile'),

    path('add-department/', addDepartment, name='addDepartment'),
    path('departments/', departments, name='departments'),
    path('departments/edit/<int:dept_id>/', editDepartment, name='editDepartment'),
    path('departments/delete/<int:dept_id>/', deleteDepartment, name='deleteDepartment'),
]