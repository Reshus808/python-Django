#self created file
from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    #return HttpResponse("welcome")
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def Sum(request):
    return render(request,"Sum.html")

def calculate(request):
    fn=request.GET.get("fn")
    sn=request.GET.get("sn")
    s=float(fn)+float(sn)
    data={'fn':fn,'sn':sn,'s':s}
    return render(request,"sresult.html",data)

def Product(request):
    return render(request,"Product.html")

def calculate1(request):
    fn=request.GET.get("fn")
    sn=request.GET.get("sn")
    p=float(fn)*float(sn)
    data={'fn':fn,'sn':sn,'p':p}
    return render(request,"presult.html",data)

def Difference(request):
    return render(request,"Difference.html")

def calculate2(request):
    fn=request.GET.get("fn")
    sn=request.GET.get("sn")
    d=float(fn)-float(sn)
    data={'fn':fn,'sn':sn,'d':d}
    return render(request,"Dresult.html",data)

def Average(request):
    return render(request,"Average.html")

def calculate3(request):
    fn=request.GET.get("fn")
    sn=request.GET.get("sn")
    a=float(fn)/float(sn)
    data={'fn':fn,'sn':sn,'a':a}
    return render(request,"Aresult.html",data)

def Contact(request):
    return render(request,"Contact.html")

def help(request):
    return render(request,"help.html")

def chk_login(request):
    email=request.GET.get('em')
    pa=request.GET.get('pa')
    if(email=="reshu@gmail.com" and pa=="rrr"):
      return render(request,"home.html")
    elif(email=="abc@gamil.com"and pa=="abc"):
      return render(request,"home.html")
    else:
      return render(request,"Error.html")
    



