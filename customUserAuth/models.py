from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserAuthModel(AbstractUser):
    user_types = models.CharField(choices=[
        ('Admin', 'Admin'),
        ('HR', 'HR'),
        ('Account', 'Account'),
        ('Employee', 'Employee'),
    ], max_length=10, null=True)
    gender = models.CharField(choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ], max_length=10, null=True, blank=True, default='Set Your Gender')

    def __str__(self):
        return self.email 
    