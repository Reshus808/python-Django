from django.urls import path
from . import views

urlpatterns = [

    path('', views.index,name="index"),
    path('Sdetails', views.Sdetails,name="Sdetails"),
    path('help', views.help,name="help"),
    path('calculate', views.calculate,name="calculate"),

]