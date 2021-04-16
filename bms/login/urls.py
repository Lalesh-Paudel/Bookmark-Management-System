from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name = 'loginP'),
    path('authenticate', views.authenticate, name = 'registerP')
]