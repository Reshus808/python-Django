from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("hello index page")
    return render(request,"sumapp/home.html")

def sum(request):
    return render(request,"sumapp/sum.html")

def calculate(request):
    fn=request.POST.get('fn')
    sn=request.POST.get('sn')
    s=float(fn)+float(sn)
    data={'fn':fn,'sn':sn,'s':s}
    return render(request,"sumapp/sresult.html",data)