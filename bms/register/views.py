from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def render_register_from(request):
    return render(request, 'Register1.html')

def register(request):
    full_name = request.POST['fullName']
    username  = request.POST['userName']
    email     = request.POST['email']
    password  = request.POST['password']
    confirm_password  = request.POST['confirm_password']

    print(full_name, username, email, password, confirm_password)

    return render(request, 'Register1.html')
