# coding:utf-8
from django.shortcuts import render,render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from .forms import LoginForm,RegistrationForm
from django.contrib import auth  
from models import Profile,HomePageNew,Vote
from numpy.f2py.auxfuncs import throw_error


def home(request):
    homenew = HomePageNew.objects.all()
    return render(request, 'home.html', {'homenew': homenew[0]})


def votes(request):
    votes = Vote.objects.all()
    return render(request, 'votes.html', {'votes': votes})

def vote_detail(request, vote_id):
    if request.method == 'POST':
        pass
    vote = get_object_or_404(Vote, pk = vote_id)
    question_list = vote.questions.all
    return render(request, 'voteDetail.html', 
                  {'vote': vote,
                   'question_list':question_list,
                   })


def register(request):
    if request.method == 'POST':# 当提交表单时
        form = RegistrationForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            user = form.save()
            return home(request)
        else:
            return render(request, 'register.html', {'form': form},  RequestContext(request))
    else:# 当正常访问时
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form},  RequestContext(request))


def logout(request):
    auth.logout(request)
    return home(request)


def login(request):
    if request.method == 'POST':# 当提交表单时
        form = LoginForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            un = form.cleaned_data['username']
            psw = form.cleaned_data['password']
            print un,psw,
            user = auth.authenticate(username=un, password=psw)  
            
            if user is not None and user.is_active:
                auth.login(request, user)
                return home(request)
            else:
                return HttpResponse("Username or Password error！")
    else:# 当正常访问时
        form = LoginForm()
    return render(request, 'login.html', {'form': form},  RequestContext(request))