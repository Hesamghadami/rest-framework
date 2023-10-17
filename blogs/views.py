from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages

def blog_home(req, cat=None, username=None):
    try :
          posts = Post.objects.filter(status=True)
          category = Category.objects.all()

          #adv = AdvertisModel.objects.all()[3]



          if username:
               posts = Post.objects.filter(client__username=username)
               
          if cat:
               posts = Post.objects.filter(category__name=cat)

          if req.GET.get('search'):
               posts = Post.objects.filter(content__contains=req.GET.get('search'))

               
          posts = Paginator(posts, 4)

          try:
               page_number = req.GET.get('page')
               posts = posts.get_page(page_number)


          except PageNotAnInteger:
               posts = posts.get_page(1)
               
          except EmptyPage:
               posts = posts.get_page(1)

               
          context = {
               'posts' : posts,
               'category' : category,
          }
          return render(req, 'blogs/Goods.html', context=context)
    except:
          return render(req, 'blogs/404.html')




def blog_single(req, pid):
    try :
        post = Post.objects.get(id=pid, status=True)
        post.counted_views += 1
        post.save()
        context = {
            'post': post,
            }
        return render(req, 'blogs/GoodsDetails.html', context=context)
    except:
        return render(req, 'blogs/404.html')




@login_required
def add(req):
     if req.method == 'GET':
          category = Category.objects.all()
          context = {
               'form' : PostForm(),
               'category':category,
          }
          return render(req,'blogs/add.html',context=context)
     elif req.method == 'POST':
          form = PostForm(req.POST, req.FILES)
          print(req.POST)
          if form.is_valid():
               form.save()
               return redirect('blog:blog_home')
          else:
               messages.add_message(req,messages.ERROR,'Input data is not valid.')
               return redirect('blog:blog_home')


# Create your views here.
