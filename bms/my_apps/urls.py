from django.contrib import admin
from django.urls import path, include
from . import views
# from renderer import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('category/', views.category, name="category"),

    path('profile/', views.profile, name="profile"),
    path('about/', views.about, name="about"),
    path('feedbacks/', views.feedback, name="feedback"),

    path('registration/', views.render_register_from, name='registration'),
    path('registration/register', views.register, name='register'),

    path('login/', views.render_login_form, name='login'),
    # path('login/authenticate', views.authenticate, name='authenticate'),

    path('remove_bookmark/', views.remove_bookmark, name="remove_bookmark"),
    path('update_bookmark/', views.update_bookmark, name="update_bookmark"),
    path('update_bookmark/update', views.update, name="update"),
    path('inputs/', views.input, name="inputs"),
    path('inputs/create_bookmark', views.create_bookmark, name="create_bookmark"),
]
