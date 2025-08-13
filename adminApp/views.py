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

#Employees

def addEmployee(request):
    return redirect('employeeList')

def employeeList(request):
    return render(request, 'employees.html')

def employeeListView(request):
    return render(request, 'employees-list.html')


#Holidays

def holiday_list(request):
    current_year = timezone.now().year
    year = int(request.GET.get('year', current_year))
    holidays = HolidayModel.objects.filter(date__year=year).order_by('date')
    
    years = list(range(current_year - 5, current_year + 6))
    
    context = {
        'holidays': holidays,
        'current_year': year,
        'years': years,
    }
    return render(request, 'holidays.html', context)


def add_holiday(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date_str = request.POST.get('date')
        
        if title and date_str:
            try:
                date_obj = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
                
                HolidayModel.objects.create(
                    title=title,
                    date=date_obj
                )
                messages.success(request, 'Holiday added successfully!')
                return redirect('holiday_list')
            except ValueError:
                messages.error(request, 'Invalid date format!')
        else:
            messages.error(request, 'Title and Date are required!')
    
    return redirect('holiday_list')


def edit_holiday(request, holiday_id):
    holiday = get_object_or_404(HolidayModel, id=holiday_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        date_str = request.POST.get('date')
        
        if title and date_str:
            try:
                # Parse the date string
                date_obj = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
                
                holiday.title = title
                holiday.date = date_obj
                holiday.save()
                messages.success(request, 'Holiday updated successfully!')
                return redirect('holiday_list')
            except ValueError:
                messages.error(request, 'Invalid date format!')
        else:
            messages.error(request, 'Title and Date are required!')
    
    context = {
        'holiday': holiday,
    }
    return render(request, 'edit_holiday.html', context)


def delete_holiday(request, holiday_id):
    holiday = get_object_or_404(HolidayModel, id=holiday_id)
    
    if request.method == 'POST':
        holiday.delete()
        messages.success(request, 'Holiday deleted successfully!')
        return redirect('holiday_list')
    
    context = {
        'holiday': holiday,
    }
    return render(request, 'delete_holiday.html', context)