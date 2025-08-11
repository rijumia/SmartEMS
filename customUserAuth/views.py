from django.shortcuts import render, redirect
from customUserAuth.models import CustomUserAuthModel
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

# Create your views here.
def homePage(request):
    return render(request, 'landing_page/home.html')

def signUp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            CustomUserAuthModel.objects.create_user(
                username = email,
                password = password,
                user_types = 'Admin',
            )
            return redirect('logIn')

    return render(request, 'register.html')

def logIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logOut(request):
    logout(request)
    return redirect('logIn')

def dashboard(request):
    return render(request, 'dashboard.html')