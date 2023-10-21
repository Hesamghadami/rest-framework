from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.http import HttpResponseRedirect



def Login(req):
    if req.user.is_authenticated:
        return redirect('/')
    elif req.method == 'GET':
        form = AuthenticationForm()
        return render(req,'registration/login.html', context={'form': form})
    elif req.method == 'POST':
            email = req.POST.get('email')
            password = req.POST.get('password')      
            user = authenticate(email=email, password=password)
            if user is not None:
                login(req,user)
                return redirect('/')
            else:
                messages.add_message(req, messages.ERROR, 'Invalid email or password')
                return redirect(req.path_info)
@login_required
def Logout(req) :
    logout(req)
    return redirect('/')



def signup(req):
    if req.user.is_authenticated:
        return redirect('/')
    elif req.method == 'GET':
        form = CustomUserCreation()
        return render(req,'registration/signup.html', context={'form': form})
    else:
            form = CustomUserCreation(req.POST,req.FILES)
            if form.is_valid():
                form.save()
                email = req.POST.get('email')
                password = req.POST.get('password1')
                user = authenticate(email=email, password=password)
                login(req,user)
                return redirect('accounts:profile')

            else:
                messages.add_message(req, messages.ERROR, 'Invalid email or password')
                return redirect(req.path_info)
            
def edit_profile(req,pid):
     prof = Profile.objects.get(id=pid)
     if req.method == 'GET':
          form = EditProfile(instance=prof)
          return render(req,'registration/edit_profile.html', context={'form': form})
     elif req.method == 'POST':
          form = EditProfile(req.POST, req.FILES ,instance=prof)
          if form.is_valid():
               form.save()
               return redirect('/') 

        
# Create your views here.
