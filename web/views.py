from django.shortcuts import render,redirect
from .models import Question
from .forms import CreateUserForm
from .forms import QuestionAddingForm
from .forms import LoginForm
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator



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


def logout_page(request):
    logout(request)
    return redirect('/')


def addQuestion(request):    
    if request.user.is_staff:
        form=QuestionAddingForm()
        if(request.method=='POST'):
            form=QuestionAddingForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'web/add_question.html',context)
    else: 
        return redirect('web:index') 


def index(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        score=0
        wrong=0
        correct=0   
        total=0
        for q in questions:
            total=total+1
            answer = request.POST.get(q.question) 
            if q.ans == answer:
                score = score+10
                correct = correct+1
            else:
                wrong = wrong+1
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total,
            
            }
        return render(request,'web/result.html',context)
    else:
        questions=Question.objects.all()
        context = {
            'questions':questions,
        }
        return render(request,'web/index.html',context)


