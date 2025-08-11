from django.urls import path
from adminApp.views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('my-profile/', profile, name='profile'),

]