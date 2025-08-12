from django.db import models
from customUserAuth.models import CustomUserAuthModel
from django.utils import timezone

# Create your models here.
class DepartmentModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class DesignationModel(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, related_name='department_info')
    
    def __str__(self):
        return self.title
    
class ProfileModel(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    user = models.OneToOneField(CustomUserAuthModel, on_delete=models.CASCADE, related_name='profile')
    employee_id = models.CharField(max_length=20, unique=True)
    full_name= models.CharField(max_length=150, null=True)
    position = models.ForeignKey(DesignationModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='designation_info')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    reports_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    
    def __str__(self):
        return f"{self.full_name}'s Profile"
    

class HolidayModel(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.title
    
    @property
    def is_past(self):
        return self.date < timezone.now().date()
    
    @property
    def day_name(self):
        return self.date.strftime('%A')