from django.db import models, reset_queries
from django.shortcuts import render
from django.http import HttpResponse
from .models import bookmarkList

# Create your views here.
def input(request):
    return render(request, 'Input.html')

def create_bookmark(request):
    site_name =     request.POST['name']
    url       =     request.POST['link']
    category  =     request.POST['category']

    print(site_name, url, category)
    bookmark = bookmarkList(site_name=site_name, url=url, category=category)
    bookmark.save()

    return render(request, 'Input.html')
