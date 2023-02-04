from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from .forms import Studentform



from .models import Student
#from .forms import Studentform

# Create your views here.

def index(request):
    return render(request,'myapp/index.html')

def signup(request):
    return render(request,"myapp/signup.html")


def check(request):
    if(request.method=="POST"):
        roll=request.POST.get('roll','')
        name=request.POST.get('name','')
        marks=request.POST.get('marks','')
        address=request.POST.get('address','')
        if(roll and name and marks and address):
            S1=Student(Roll=roll,Name=name,Marks=marks,Address=address)
            S1.save()
        else:
            return HttpResponse("Invalid data")
            return render(request,'myapp/display_rec.html')




def display_rec(request):
    students=Student.objects.all()
    data={'students':students}
    return render(request,'myapp/display_rec.html',data)

def deletedisplay(request):
    S1=Student.objects.all()
    data={'S1':S1}
    return render(request,'myapp/delete_rec.html',data)

def deleterecord(request,id):
    studentsdel = Student.objects.get(id = id)
    studentsdel.delete()
    #after deleting display all the records
    S1=Student.objects.all()
    data={'S1':S1}
    return render(request,'myapp/delete_rec.html',data)

def updatedisplay(request):
    S1=Student.objects.all()
    data={'S1':S1}
    return render(request,'myapp/update_rec.html',data)


def editrecord(request,id):
    student=Student.objects.get(id=id)
    data={'Student':student}
    print("edit called")
    print(id);
    #return HttpResponse("Hello edit called")
    return render(request,'myapp/editrecord.html',data)

def updaterecord(request,id):
    studentsupdate = Student.objects.get(id = id)
    form=Studentform(request.POST,instance=studentsupdate)
    if(form.is_valid()):
        form.save()
        data={'student':studentsupdate}
        messages.success(request,"Record Updated .... !")
        #return render(request,"myapp/editrecord.html",data)
        #return render(request,'myapp/updatedisplay.html',data)
        return redirect("updatedisplay")
    #return HttpResponse('hello')

