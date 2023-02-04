#self created file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("welcome")
    return render(request,"index.html")

def Std_details(request):
    fn=request.GET.get('fn')
    mn=request.GET.get('mn')
    ln=request.GET.get('ln')
    
    email=request.GET.get('email')
    address=request.GET.get('address')
    contact=request.GET.get('contact')

    gen=request.GET.get('gender')
    college=request.GET.get('college')
    branch=request.GET.get('branch')
    eq=request.GET.get('eq')


    city=request.GET.get('city')
    state=request.GET.get('state')
    zip=request.GET.get('zip')

    m1=request.GET.get('m1')
    m2=request.GET.get('m2')
    m3=request.GET.get('m3')
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

    
    data={'fn':fn,'mn':mn,'ln':ln,
    'gen':gen,'college':college,'branch':branch,
    'city':city,'state':state,'zip':zip,
    'email':email,'address':address,'contact':contact,
    'eq':eq,'m1':m1,'m2':m2,'m3':m3,
    'total':total,'per':per,'grade':grade}

    return render(request,"details.html",data)
    