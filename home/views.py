from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from blogs.models import Post, Category 
from .forms import *

def home(req, cat=None):
    if req.method == 'GET':
        posts = Post.objects.filter(status=True)
        category = Category.objects.all()
        last_nine_posts = posts[:9]
        if cat:
            posts = Post.objects.filter(category__name=cat)

        context = {
        'posts' : posts,
        'category' : category,
        'last_nine_posts' : last_nine_posts,
        }
        return render(req, 'home/index.html', context=context)
        
    

    elif req.method == 'POST':
        form = NewsLetterForm(req.POST)
        if form.is_valid():
            form.save()   
            return redirect('/')
        
    

def contact(req):
    if req.method == 'GET':
        return render(req, 'home/index.html')
    
    elif req.method == 'POST':
        form_contact = ContactUsForm(req.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect('/')
        
    
    
    


# Create your views here.
