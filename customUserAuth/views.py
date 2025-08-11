from django.shortcuts import render, redirect
from customUserAuth.models import CustomUserAuthModel
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def homePage(request):
    return render(request, 'landing_page/home.html')

def signUp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return render(request, 'register.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        if CustomUserAuthModel.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'register.html')

        CustomUserAuthModel.objects.create_user(
            username=email,
            password=password,
            user_types='Admin',
        )
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('logIn')

    return render(request, 'register.html')


def logIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Email and password are required.")
            return render(request, 'login.html')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, 'login.html')

def logOut(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('logIn')


def dashboard(request):
    return render(request, 'dashboard.html')