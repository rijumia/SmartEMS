from django.shortcuts import render, redirect
from adminApp.models import *
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
def profile(request):
    return render(request, 'profile.html')

def addDepartment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        if name:
            DepartmentModel.objects.create(
                name = name,
                description = description,
            )
            messages.success(request, 'Department added successfully!')
            return redirect('departments')
        else:
            messages.error(request, 'Department name is required!')
    
    return redirect('departments')
def departments(request):
    departments = DepartmentModel.objects.all().order_by('id')
    return render(request, 'departments/departments.html',{'departments':departments})
def editDepartment(request, dept_id):
    department = DepartmentModel.objects.get(id=dept_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        
        if name:
            department.name = name
            department.description = description
            department.save()
            messages.success(request, 'Department updated successfully!')
            return redirect('departments')
        else:
            messages.error(request, 'Department name is required!')
    
    context = {
        'department': department,
    }
    return render(request, 'departments/editDepartment.html', context)

def deleteDepartment(request, dept_id):
    department = DepartmentModel.objects.get(id=dept_id)
    
    if request.method == 'POST':
        if department.department_info.exists():
            messages.error(request, 'Cannot delete department with existing designations!')
            return redirect('departments')
        
        department.delete()
        messages.success(request, 'Department deleted successfully!')
        return redirect('departments')
    
    context = {
        'department': department,
    }
    return render(request, 'departments/deleteDepartment.html', context)