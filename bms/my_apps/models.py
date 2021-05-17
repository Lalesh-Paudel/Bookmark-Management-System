from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.shortcuts import resolve_url
from numpy import mod

# Create your models here.

class UserAuthenticationList(models.Model):
    full_name = models.CharField(max_length=200)
    username  = models.CharField(max_length=200)
    email     = models.EmailField(max_length=200)
    password  = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class CurrentLogedInUser(models.Model):
    admin = models.ForeignKey(UserAuthenticationList, on_delete=CASCADE)


class bookmarkList(models.Model):
    # admin = models.ForeignKey(UserAuthenticationList, on_delete=CASCADE)

    site_name = models.CharField(max_length=200)
    url       = models.URLField(max_length=500)
    category  = models.CharField(max_length=200)

    def __str__(self):
        return self.site_name