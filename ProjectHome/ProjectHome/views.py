#self created file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("welcome")
    return render(request,"index.html")

def analyze(request):
    txt=request.POST.get('txt')
    chk1=request.POST.get('chk1','off')
    chk2=request.POST.get('chk2','off')
    chk3=request.POST.get('chk3','off')
    print(txt)
    print(chk1)

    if(chk1=="on"):
        punctuations='''!()-[]{};:'"=,/<\>.@#$%^&*_~'''
        final=""
        for i in txt:
            if(i not in punctuations):
                final+=i
        data={'purpose':'Remove Punctuations','final':final}
        return render(request,"result.html",data)

    elif(chk2=="on"):
        final=txt.upper()
        data={'purpose':'Convert To Uppercase','final':final}
        return render(request,"result.html",data)

    elif(chk3=="on"):
        final=txt.lower()
        data={'purpose':'Convert To Lowercase','final':final}
        return render(request,"result.html",data)

    else:
        return render(request,"Error.html")
        #return HttpResponse("Error")

def Aboutus(request):
    return render(request,"Aboutus.html")

def Contact(request):
    return render(request,"Contact.html")
        