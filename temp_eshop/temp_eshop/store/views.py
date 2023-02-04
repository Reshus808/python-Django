from django.shortcuts import render
# Create your views here.
#self
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Category
from .models import Image
from .models import Customer
from .models import Contact
from .models import Orders
from .models import OrderUpdate
import json


##
def index(request):
    return render(request,"index.html")


def showhome(request):
    images = Image.objects.all()
    cats = Category.objects.all()
    data={'images':images,'cats':cats}
    #return render(request,'home.html',data)
    #return render(request,'home1.html',data)
    #return render(request,'home2.html',data)
    #return render(request,'home3.html',data)
    #return render(request,'home4.html',data)
    #return render(request,'home5.html',data)
    #return render(request,'home6.html',data)
    #return render(request,'home7.html',data)
    #return render(request,'home8.html',data)
    return render(request,'home9.html',data)


def display_by_category(request,cid):
    print(cid)
    cats = Category.objects.all()
    #just to get the category that has been selected
    category=Category.objects.get(pk=cid)
    #now to get the images as per the selected category
    images = Image.objects.filter(cat=category)
    data={'images':images,'cats':cats}
    return render(request,'home.html',data)


def signup(request):
    if(request.method=="GET"):
        return render(request,"signup.html")
    if(request.method=="POST"):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        #validations
        error_message=None
        if not first_name:
            error_message="!!! First Name Required !!!"
        elif(len(first_name) < 4):
            error_message="!!! First Name Must be Min 4 chars long !!!"
        elif not last_name:
            error_message="!!! Last Name Required !!!"
        elif(len(last_name) < 4):
            error_message="!!! Last Name Must be Min 4 chars long !!!"
        elif not phone:
            error_message="!!! Phone No Required !!!"
        elif(len(phone) < 10):
            error_message="!!! Phone No Min 10 Digits Long !!!"
        elif not password:
            error_message="!!! Password No Required !!!"
        elif(len(phone) < 6):
            error_message="!!! Password Min 6 chars !!!"
        data={'error':error_message}
        #to save data if all is fine
        if(not error_message):
            customer = Customer(first_name = first_name,
                        last_name= last_name,
                        phone= phone,
                        email= email,
                        password=password)
            customer.save()
        #if all is fine we have to call index page
            return redirect("index") # name of index page ("index.html")
        else:
            return render(request,"signup.html",data)
        

def aboutus(request):
    return render(request,"aboutus.html")

def projecthelp(request):
    return render(request,"project_help.html")

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        print(name,email,phone, desc )
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,"contact.html")
    #return redirect("contact")


def search(request):
    return render(request,"search.html")


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})
    return render(request, 'checkout.html')


#def traker(request):
def tracker(request):
    if(request.method=="GET"):
        return render(request,"traker.html")
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        print(orderId,email)
        order = Orders.objects.get(order_id=orderId)
        print(order,order.email)
        if(order.email==email):
            update = OrderUpdate.objects.filter(order_id=orderId)
            order = Orders.objects.get(order_id=orderId)
            data={'updates':update,'order':order}
            return render(request,'tracker_data.html',data)

    return HttpResponse("Hello")

            
            
    #         if len(order)>0:
    #             print("rec found",len(order))
    #             update = OrderUpdate.objects.filter(order_id=orderId)
    #             print(update)
    #             data={'updates':update}
    #             return render(request,'tracker_data.html',data)
    #         else:
    #             return HttpResponse('no rec found')
    #     except Exception as e:
    #         return HttpResponse('error')
    #     return HttpResponse("Hello")
    
    # return HttpResponse("Hi")
    #     try:
    #         order = Orders.objects.filter(order_id=orderId, email=email)
    #         if len(order)>0:
    #             update = OrderUpdate.objects.filter(order_id=orderId)
    #             #data={'students':students}
    #             #return render(request,'stdapp/displayall.html',data)
    #         else:
    #             return HttpResponse('{}')
    #     except Exception as e:
    #         return HttpResponse('{}')
    # return render(request,"traker.html")

    # if request.method=="POST":
    #     orderId = request.POST.get('orderId', '')
    #     email = request.POST.get('email', '')
    #     try:
    #         order = Orders.objects.filter(order_id=orderId, email=email)
    #         if len(order)>0:
    #             update = OrderUpdate.objects.filter(order_id=orderId)
    #             updates = []
    #             for item in update:
    #                 updates.append({'text': item.update_desc, 'time': item.timestamp})
    #                 response = json.dumps(updates, default=str)
    #             return HttpResponse(response)
    #         else:
    #             return HttpResponse('{}')
    #     except Exception as e:
    #         return HttpResponse('{}')

    # #return render(request, 'tracker.html')
    # return render(request,"traker.html")


def productview(request,id):
    #fetch the product using the id
    product = Image.objects.get(id = id)
    print(product)
    data={'product':product}

    return render(request,"productview.html",data)

def clearcart(request):
    return render(request,"clearcart.html")