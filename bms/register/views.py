from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def render_register_from(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        print ("Lauda lassan jhfjshjhdfj sfhjshdjhskjdhjks d working")
    # if form.is_valid():
    #     form.save()
    #     return redirect('login')
    # else:
    #     form = UserCreationForm()
    return render(request, 'Register1.html',{})

def register(request):
    full_name = request.POST['fullName']
    username  = request.POST['userName']
    email     = request.POST['email']
    password  = request.POST['password']
    confirm_password  = request.POST['confirm_password']

    print(full_name, username, email, password, confirm_password)

    return render(request, 'Register1.html')
