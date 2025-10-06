from django.urls import path
from .views import *
urlpatterns = [
    path("",Home,name="home"),
    path("login", Login,name="user_login"),
    path("signup",Signup,name="user_signup")
]

