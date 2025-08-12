from django.shortcuts import render, redirect, get_object_or_404
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

def designation_list(request):
    designations = DesignationModel.objects.select_related('department').all().order_by('department__name', 'title')
    departments = DepartmentModel.objects.all()
    
    context = {
        'designations': designations,
        'departments': departments,
    }
    return render(request, 'departments/designations.html', context)


def add_designation(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        department_id = request.POST.get('department')
        
        if title and department_id:
            try:
                department = DepartmentModel.objects.get(id=department_id)
                DesignationModel.objects.create(
                    title=title,
                    department=department
                )
                messages.success(request, 'Designation added successfully!')
                return redirect('designation_list')
            except DepartmentModel.DoesNotExist:
                messages.error(request, 'Invalid department selected!')
        else:
            messages.error(request, 'Title and Department are required!')
    
    return redirect('designation_list')


def edit_designation(request, desig_id):
    designation = get_object_or_404(DesignationModel, id=desig_id)
    departments = DepartmentModel.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        department_id = request.POST.get('department')
        
        if title and department_id:
            try:
                department = DepartmentModel.objects.get(id=department_id)
                designation.title = title
                designation.department = department
                designation.save()
                messages.success(request, 'Designation updated successfully!')
                return redirect('designation_list')
            except DepartmentModel.DoesNotExist:
                messages.error(request, 'Invalid department selected!')
        else:
            messages.error(request, 'Title and Department are required!')
    
    context = {
        'designation': designation,
        'departments': departments,
    }
    return render(request, 'departments/edit_designation.html', context)


def delete_designation(request, desig_id):
    designation = get_object_or_404(DesignationModel, id=desig_id)
    
    if request.method == 'POST':
        if designation.designation_info.exists():
            messages.error(request, 'Cannot delete designation with existing employees!')
            return redirect('designation_list')
        
        designation.delete()
        messages.success(request, 'Designation deleted successfully!')
        return redirect('designation_list')
    
    context = {
        'designation': designation,
    }
    return render(request, 'departments/delete_designation.html', context)