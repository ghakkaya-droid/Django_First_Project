from django.urls import path
from . import views
urlpatterns = [
    path("index", views.index, name="index"),
    #path("python_course", views.python_course, name="python_course"),
    #path("java_course", views.java_course, name="java_course"),
    path("<str:item>", views.course, name="course")
]