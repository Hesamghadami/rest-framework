from django import forms
from .models import *


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['title', 'client_url', 'client', 'content', 'image1', 'image2', 'image3', 'published_date', 'category']

