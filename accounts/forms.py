from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import CustumUser
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    image = forms.ImageField()


    class Meta:
        model = CustumUser
        fields = ['email','password1', 'password2']

class CaptchaForm(forms.Form):
    captcha = CaptchaField()