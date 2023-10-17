from django.urls import path
from .views import *


app_name = 'courses'

urlpatterns = [
    path("", courses,name='courses'),
    path("category/<str:cat>",courses,name="course_cat"),
    path("teacher/<str:teacher>",courses,name="course_teacher"),
    path("search/",courses,name="course_search"),
    path("course-detail/<int:id>",course_detail,name="course_detail"),
    path("<int:id>",delete_comment,name="delete"),
    path("edit/comment/<int:id>",edit,name="edit"),
    path("comment/reply/<int:id>",reply,name="reply"),
]