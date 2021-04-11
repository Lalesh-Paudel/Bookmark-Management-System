from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login1.html')


def register(request):
    return render(request, 'register1.html')


def input(request):
    return render(request, 'input.html')
