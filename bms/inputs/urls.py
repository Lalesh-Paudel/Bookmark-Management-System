from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.input, name="inputs"),
    path('create_bookmark', views.create_bookmark, name="create_bookmark"),
]