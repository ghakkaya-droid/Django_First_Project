from django.urls import path
from . import views
urlpatterns = [
    path("index", views.index, name="index"),
    path("",views.index,name="main"),
    path("<int:num1>",views.course_number_view,name="course_number"),
    #path("python_course", views.python_course, name="python_course"), #***webSite.com/first_app/python_course
    #path("java_course", views.java_course, name="java_course"), #***webSite.com/first_app/java_course
    path("<str:item>", views.course, name="course"), #***webSite.com/first_app/"değişken"
    path("<int:num1>/<int:num2>/",views.multiply_view,name="multiply"), #***webSite.com/first_app/"Sayı-1"/"Sayı-2"/
     
]