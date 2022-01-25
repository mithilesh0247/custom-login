from datetime import datetime
from itertools import count
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.decorators import login_required
from Login.models import count_user
import json
# Create your views here.

@login_required(login_url='login/')
def home(request):
    return render(request,"home.html")       

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            countd = count_user.objects.filter(username=username)
            if len(countd)>0:
                data = count_user.objects.get(username=username)
                data.count += 1
                time = json.loads(data.loginAt)
                time.append(str(datetime.now()))   
                data.loginAt = json.dumps(time)
                data.save()
            else:
                data = count_user(username=username,count=1,loginAt=json.dumps([str(datetime.now())]))
                data.save()    
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')