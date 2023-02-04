from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("welcome myapp")
    return render(request,"myapp/home.html")

def addrecord(request):
    return render(request,"myapp/addrecord.html")

def displayall(request):
    return render(request,"myapp/displayall.html")

def delete(request):
    return render(request,"myapp/delete.html")

def update(request):
    return render(request,"myapp/update.html")