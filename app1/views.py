from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def custom_login_view(request):
    return render(request, 'app1/login.html')
