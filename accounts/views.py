from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreation
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomeUser
from .forms import CaptchaForm




def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = AuthenticationForm()
        captcha = CaptchaForm()
        return render(request,'registration/login.html', context={'form': form,'captcha': captcha})
    elif request.method == 'POST':
        captcha_form = CaptchaForm(request.POST)
        if captcha_form.is_valid():

            
            email = request.POST.get('email').strip()
            password = request.POST.get('password')      
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid email or password')
                return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, 'Invalid captcha')
            return redirect(request.path_info)


@login_required
def Logout(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        captcha = CaptchaForm()
        form = CustomUserCreation()
        return render(request,'registration/signup.html', context={'form': form,'captcha': captcha})
    else:
        captcha_form = CaptchaForm(request.POST)
        if captcha_form.is_valid():
            form = CustomUserCreation(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                email = request.POST.get('email')
                password = request.POST.get('password1')
                user = authenticate(email=email, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.add_message(request, messages.ERROR, 'Invalid email or password')
                    return redirect(request.path_info)
            else:
                messages.add_message(request, messages.ERROR, 'Invalid email or password')
                return redirect(request.path_info)
            
        else:
            messages.add_message(request, messages.ERROR, 'Invalid captcha')
            return redirect(request.path_info)

        


# Create your views here.
