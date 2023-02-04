from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    #return HttpResponse("welcome")
    return render(request,"login.html")

def chk_login(request):
    em=request.POST.get('em')
    pa=request.POST.get('pa')

    if(em=="reshu40@gmail.com" and pa=="RRR"):
      return render(request,"index.html")
    elif(em=="reshu44@gmail.com" and pa=="rrr"):
      return render(request,"index.html")
    else:
        return render(request,"error.html")

def index(request):
    return render(request,"index.html")

def Aboutus(request):
    return render(request,"Aboutus.html")

def Contactus(request):
    return render(request,"Contactus.html")

def ourservices(request):
    return render(request,"ourservices.html")