#self created file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("welcome to index page")
    return render(request,"index.html")
    
def login(request):
    return render(request,"login.html")

def chk_login(request):
    email=request.POST.get('em')
    pa=request.POST.get('pa')
    
    if(email=="reshu40@gmail.com" and pa=="RRR"):
        return render(request,"index.html")
    elif(email=="resu@gmail.com" and pa=="rrr"):
        return render(request,"index.html")
    else:
        return render(request,"Error.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")

def help(request):
    return render(request,"help.html")


    

