from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("hye")
    return render(request,"student/index.html")

def Sdetails(request):
    return render(request,"student/Sdetails.html")

def calculate(request):
    fn=request.POST.get('fn')
    mn=request.POST.get('mn')
    ln=request.POST.get('ln')

    gen=request.POST.get('gender')
    eq=request.POST.get('eq')
    college=request.POST.get('college')
    branch=request.POST.get('branch')
    m1=request.POST.get('m1')
    m2=request.POST.get('m2')
    m3=request.POST.get('m3')
    total=float(m1)+float(m2)+float(m3)
    per=total/3
    
    if(per>=90):
        grade="A+"
    elif(per>=80):
        grade="A"
    elif(per>=70):
        grade="B+"
    elif(per>=60):
        grade="B"
    elif(per>=50):
        grade="C"
    elif(per>=40):
        grade="D"
    else:
        grade="F"


    data={'fn':fn,'mn':mn,'ln':ln,'gen':gen,'eq':eq,
    'college':college,'branch':branch,
    'm1':m1,'m2':m2,'m3':m3,'total':total,'per':per,'grade':grade}
        
    return render(request,"student/Sresult.html",data)

def help(request):
    return render(request,"student/help.html")

def Aboutus(request):
    return render(request,"student/Aboutus.html")
