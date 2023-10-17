from django import forms
from .models import *


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ['email']

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']