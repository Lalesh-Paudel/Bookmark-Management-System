from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField

# Create your models here.

class UserInfo(models.Model):
    full_name       =    models.CharField(max_length=50)
    username        =    models.CharField(max_length=50)
    email           =    models.EmailField(max_length=200)
    password        =    models.CharField(max_length=40)
    login_status    =    models.BooleanField(default=False)

    def get_full_name(self):
        pass
    
    def get_username(self):
        pass

    def get_email(self):
        pass

    def get_passwrod(self):
        pass

    def get_login_status(self):
        pass


class user(models.Model):
    UserInfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

