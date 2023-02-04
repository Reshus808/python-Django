from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Category
from .models import Image
from .models import Customer
 

def home(request):
    return render(request,'myapp/home.html') 



def showhome(request):
    images = Image.objects.all()
    cats = Category.objects.all()
    data={'images':images,'cats':cats}
    #return render(request,'home.html',data)
    return render(request,'myapp/home.html',data)
    #return render(request,'home2.html',data)
    #return render(request,'home3.html',data)
    #return render(request,'home4.html',data)
    #return render(request,'home5.html',data)

def display_by_category(request,cid):
    print(cid)
    
    cats = Category.objects.all()
    #just to get the category that has been selected
    category=Category.objects.get(pk=cid)
    #now to get the images as per the selected category
    images = Image.objects.filter(cat=category)

    data={'images':images,'cats':cats}
    return render(request,'myapp/home.html',data)


def signup(request):
    return render(request,'myapp/signup.html')


def aboutus(request):
    return render(request,'myapp/aboutus.html')


def contactus(request):
    return render(request,'myapp/contact.html')

def projecthelp(request):
    return render(request,'myapp/project_help.html')

def signup(request):
    if(request.method=="GET"):
        return render(request,"myapp/signup.html")
    if(request.method=="POST"):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

