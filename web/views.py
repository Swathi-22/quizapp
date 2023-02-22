from django.shortcuts import render,redirect
from .models import Question
from .forms import CreateUserForm
from .forms import LoginForm
from django.contrib.auth import login,logout,authenticate




def signup(request):
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('web:signin')
    context = {"form":form,}
    return render(request,'web/register.html',context)


def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if request.user.is_authenticated:
            return redirect('web:index')
        elif user is not None:
            login(request,user)
            return redirect('/')
    context = {}
    return render(request,'web/login.html',context)


def logout(request):
    context = {}
    return render()


def index(request):
    context = {}
    return render(request,'web/index.html',context)


