from django.urls import path
from . import views

urlpatterns=  [
    path('', views.home,name="home"),
    path('sum', views.sum,name="sum"),
    path('calculate', views.calculate,name="calculate"),

    
]