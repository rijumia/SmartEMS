from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'landing_page/home.html')

def signUp(request):
    return render(request, 'register.html')

def logIn(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')