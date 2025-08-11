from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
def profile(request):
    return render(request, 'profile.html')