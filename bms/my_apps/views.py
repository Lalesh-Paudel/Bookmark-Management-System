from django.apps.config import AppConfig
from django.db.models.manager import BaseManager
from django.shortcuts import render
from django.http import HttpResponse
from .models import UserAuthenticationList, CurrentLogedInUser, bookmarkList
from . import operations

# Create your views here.
def Home(request):
    my_content = {
        "categories": operations.get_categories(),
        "bookmarks": operations.get_bookmarks('all'),
    }

    return render(request, 'Home.html', my_content)

def profile(request):
    return render(request, 'Profile.html')

def about(request):
    return render(request, 'About.html')

def feedback(request):
    return render(request, 'Feedback.html')

def render_register_from(request):
    return render(request, 'Register1.html')

def register(request):
    full_name = request.POST['fullName']
    username  = request.POST['userName']
    email     = request.POST['email']
    password  = request.POST['password']
    confirm_password  = request.POST['confirm_password']

    # if password == confirm_password:
    #     new_user = UserAuthenticationList(full_name=full_name, username=username, email=email, password=password)
    #     CurrentLogedInUser.admin = new_user
    #     new_user.save()
    #     CurrentLogedInUser.save()

    return render(request, 'Register1.html')

def authenticate(request):
    usernae = request.POST['username']
    password = request.POST['password']

    # for user in UserAuthenticationList.objects.all():
    #     if (user.username == usernae) and  (user.password == password):
    #         CurrentLogedInUser.objects.all().delete()
    #         new_admin = CurrentLogedInUser()
    #         new_admin.admin = user
    return render(request, 'login1.html', {})

def render_login_form(request):

    return render(request, 'login1.html', {})

def input(request):
    return render(request, 'Input.html')


def create_bookmark(request):
    site_name =     request.POST['name']
    url       =     request.POST['link']
    category  =     request.POST['category']

    bookmark = bookmarkList(site_name=site_name, url=url, category=category)
    bookmark.save()

    return render(request, 'Input.html')


def remove_bookmark(request):
    id = request.GET['id']
    bookmarkList.objects.filter(id=id).delete()

    my_content = {
        "bookmarks": operations.get_bookmarks('all'),
    }

    return render(request, 'Home.html', my_content)


def update_bookmark(request):
    global current_bookmark_choosen_id 
    current_bookmark_choosen_id = request.GET['id']

    my_content = {
        "choosen_bookmark": bookmarkList.objects.get(id=current_bookmark_choosen_id),
    }

    return render(request, 'update_bookmark.html', my_content)


def update(request):
    current_bookmark = bookmarkList.objects.get(id=current_bookmark_choosen_id)

    site_name =     request.POST['name']
    url       =     request.POST['link']
    category  =     request.POST['category']

    current_bookmark.site_name = site_name
    current_bookmark.url = url
    current_bookmark.category = category

    current_bookmark.save()

    my_content = {
        "bookmarks": operations.get_bookmarks('all'),
    }

    return render(request, 'Home.html', my_content)


def category(request):
    category_name = request.GET['category']

    my_content = {
        "categories": operations.get_categories(),
        "bookmarks": operations.get_bookmarks(category_name),
    }

    return render(request, 'Home.html', my_content)