#self created file
from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    #return HttpResponse("welcome")
   return render(request,"login.html")

def home(request):
     return render(request,"home.html")

def check(request):
    email=request.GET.get('em')
    pa=request.GET.get('pa')
    if(email=="reshu@gmail.com" and pa=="rrr"):
      return render(request,"home.html")
    elif(email=="abc@gamil.com"and pa=="abc"):
      return render(request,"home.html")
    else:
      return render(request,"error.html")

def aboutus(request):
    return render(request,"aboutus.html")


def contact(request):
    return render(request,"contact.html")
    
def dove(request):
     return render(request,"product_details_dove.html")

def lux(request):
     return render(request,"product_details_lux.html")

def Forget(request):
     return render(request,"right_pass.html")



    
    
