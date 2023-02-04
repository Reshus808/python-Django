from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("renu")
    return render(request,"product/index.html")

def chk_product(request):
    pn=request.POST.get('pn')
    pc=request.POST.get('pc')
    pb=request.POST.get('pb')

    pq=request.POST.get('pq')
    mfd=request.POST.get('mfd')
    pu=request.POST.get('pu')
    
    data={'pn':pn,'pc':pc,'pb':pb,'pq':pq,
    'mfd':mfd,
    'pu':pu}
        
    return render(request,"product/Presult.html",data)

def help(request):
    return render(request,"product/help.html")

def Pdetails(request):
    return render(request,"product/Pdetails.html")
