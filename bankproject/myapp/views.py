from django.shortcuts import render
from .models import Customer
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request,'bankapp/index.html')


def signup(request):
    return render(request,'bankapp/signup.html')


def display_rec(request):
    return render(request,'bankapp/display_rec.html')



def check(request):
    if(request.method=="POST"):
        accountno=request.POST.get('accountno')
        name=request.POST.get('name')
        balance=request.POST.get('balance')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        street=request.POST.get('street')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')
        if(accountno and name and balance and mobile and email and password and street and city and state and country):
                    C1=C1(accountno=accountno,
                    name=name,
                    balance=balance,
                    mobile=mobile,
                    email=email,
                    password=password,
                    street=street,
                    city=city,
                    state=state,
                    country=country)
                    C1.save()
        else:
            return render(request,"bankapp/signup.html",data)
        #validations
        # error_message=None
        # if not acno:
        #     error_message="!!! Account Number Required !!!"
        # elif(len(acno)<10):
        #     error_message="!!! Account Number Must be Min 10 chars long !!!"
        # elif not name:
        #     error_message="!!! Name Required !!!"
        # elif(len(name)<4):
        #     error_message="!!! Name Must be Min 4 chars long !!!"
        # elif not balance:
        #     error_message="!!! Balance Required !!!"
        # elif(len(balance)<2):
        #     error_message="!!! Name Must be Min 2 number long !!!"
        # elif not mobile:
        #     error_message="!!! Mobile No Required !!!"
        # elif(len(mobile)<10):
        #     error_message="!!! Mobile No Min 10 Digits Long !!!"
        # elif not password:
        #     error_message="!!! Password No Required !!!"
        # elif(len(password)<6):
        #     error_message="!!! Password Min 6 chars!!!"
        # elif not street:
        #     error_message="!!! Street Name Required !!!"
        # elif(len(street)<6):
        #     error_message="!!! Street Name Must be Min 6 chars long !!!"
        # elif not city:
        #     error_message="!!! City Name Required !!!"
        # elif(len(city)<6):
        #     error_message="!!! City Name Must be Min 6 chars long !!!"
        # elif not state:
        #     error_message="!!! State Name Required !!!"
        # elif(len(state)<3):
        #     error_message="!!! State Name Must be Min 3 chars long !!!"
        # elif not country:
        #     error_message="!!! Country Name Required !!!"
        # elif(len(country)<3):
        #     error_message="!!! Country Name Must be Min 3 chars long !!!"
        # else:
        #     cust=Customer.objects.filter(email=email)
        #     if cust:
        #         error_message="Record with emailId already present"
        # data={'error':error_message}
        # #to save data if all is fine
        # if(not error_message):


#def register(request):
 #   return render(request,"signup.html")
