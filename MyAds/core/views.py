from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import JsonResponse
from .forms import CreateUser
from .models import MyUser
from django.contrib.auth import authenticate,login
# Create your views here.


def Home(request):
    return render(request,"core/home.html")
def showAds(request):
    if(request.method == "POST"):
        return JsonResponse(data={"url":"https://www.revenuecpmgate.com/cszdcei7?key=c254bc2e84cb7b8575e14c6427be862d"})
    return render(request,"core/ads.html")

def Signup(request):
    forms = CreateUser()
    if(request.method == "POST"):
        forms = CreateUser(request.POST)
        if(forms.is_valid()):
            user = MyUser(username=request.POST.get('username'))
            user.set_password(request.POST.get("password1"))
            user.save()
            return redirect(reverse("core_ads"))
        print(forms.errors)
    return render(request,"user/signup.html",{'form':forms})

def UserLogin(request):
    error = False
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        auth =authenticate(request,username=user,password=password)
        if(auth):
            login(request,auth)
            return redirect(reverse("core_ads"))
        error = True
    return render(request,"user/login.html",{"error":error})