from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_register_from, name='registration'),
    path('register', views.register, name='register')
]