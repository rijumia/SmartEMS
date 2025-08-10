from django.urls import path
from customUserAuth.views import *

urlpatterns = [
    path('', homePage, name='home'),
    path('log-in/', logIn, name='logIn'),
    path('register/', signUp, name='signUp'),

    path('dashboard/', dashboard, name='dashboard'),
]