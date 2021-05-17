from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login1.html',{'form':form})


def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username, password)

    return render(request, 'login1.html')
