from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,"index.html")
def signup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("password")
        pass2=request.POST.get("password2")
        if User.objects.filter(username=uname).exists():
            return HttpResponse("username already exists")
        if pass1!=pass2:
            return HttpResponse("password doesn't match")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect("login")
    return render(request,"signup.html")
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return HttpResponse("username and password is Incorrect")

    

    else:
        return render(request,"login.html")
def logoutuser(request):
    logout(request)
    return render(request,"login.html")