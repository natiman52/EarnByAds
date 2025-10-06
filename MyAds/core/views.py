from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import CreateUser
from .models import MyUser
from django.contrib.auth import authenticate
# Create your views here.


def Home(request):
    return render(request,"core/home.html")
def showAds(request):
    return render(request,"core/ads.html")

def Signup(request):
    forms = CreateUser()
    if(request.method == "POST"):
        forms = CreateUser(request.POST)
        if(forms.is_valid()):
            user = MyUser(username=request.POST.get('username'))
            user.set_password(request.POST.get("password1"))
            user.save()
            return redirect(reverse("user_login"))
        print(forms.errors)
    return render(request,"user/signup.html",{'form':forms})

def Login(request):
    error = None
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        auth =authenticate(request,username=user,password=password)
        if(auth):
            return redirect(reverse("home"))
        error = True
    return render(request,"user/login.html",{"error":error})