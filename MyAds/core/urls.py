from django.urls import path
from .views import *
urlpatterns = [
    path("",Home,name="home"),
    path('show',showAds,name="core_ads"),
    path("login", Login,name="user_login"),
    path("signup",Signup,name="user_signup")
]

