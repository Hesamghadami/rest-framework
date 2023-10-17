from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser

from captcha.fields import CaptchaField


class CustomUserCreation(UserCreationForm):



    class Meta:
        model = CustomeUser
        fields = [ 'email', 'password1', 'password2']


class CaptchaForm(forms.Form):
    captcha = CaptchaField()