from django.urls import path
from .views import *


app_name = 'blog'


urlpatterns = [
    path('', blog_home , name= 'blog_home'),
    path('post_details/<int:pid>', blog_single , name='blog_single'),
    path('author/<str:username>', blog_home , name= 'blog_home_with_username'),
    path('category/<str:cat>', blog_home , name= 'blog_home_with_category'),
    path('search/', blog_home , name= 'blog_home_with_search'),
    path('add/', add , name='add'),
]