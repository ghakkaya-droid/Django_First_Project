from django.shortcuts import render
from django.http import HttpResponse

course_dictionary = {
    "python": "Python Course Page",
    "java": "Java Course Page",
    "kotlin": "Kotlin Course Page",
    "swift": "Swift Course Page"
}

def course(request,item):
    return HttpResponse(course_dictionary.get(item,"Not Found"))


def index(request):
    return HttpResponse("This is first Django project, first index")

#def python_course(request):
#    return HttpResponse("Python Course Page")

#def java_course(request):
#    return HttpResponse("Java Course Page")
