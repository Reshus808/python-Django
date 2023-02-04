from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentForm
from .models import Student

# Create your views here.

def add(request):
    # return HttpResponse('this is appp')
    form = StudentForm(request.POST or None)
    student = Student.objects.all()
    if form.is_valid():
       form.save()
    return render(request, 'home.html', {'form':form})

def editData(request, id):
    # return HttpResponse('this is edit')
    student = Student.objects.get(id = id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'edit.html', {'student': student})

def show(request):
    # return HttpResponse('this is about')
    student = Student.objects.all()
    return render(request, 'show.html', {'student':student})

def delete(request, id):
    # return HttpResponse('this is about')

    form = Student.objects.get(id = id)
    form.delete()
    return HttpResponseRedirect('/')
