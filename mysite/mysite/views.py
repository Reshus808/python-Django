from django.shortcuts import render;
from django.http import HttpResponse


def index(request):
    # return HttpResponse('hello old')
    return render(request, "index.html")



def Courses(request):
    return HttpResponse('courses page')

def courseDetails(request, courseId):
    return HttpResponse(courseId)
