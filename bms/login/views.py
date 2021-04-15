from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'login1.html')


def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username, password)

    return render(request, 'login1.html')
