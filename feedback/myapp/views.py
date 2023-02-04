from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')


def display(request):
    return render(request,'myapp/display.html')
