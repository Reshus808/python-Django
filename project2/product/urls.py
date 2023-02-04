from django.urls import path
from . import views

urlpatterns = [

    path('', views.index,name="index"),
    path('chk_product', views.chk_product,name="chk_product"),
    path('help', views.help,name="help"),
    path('Pdetails', views.Pdetails,name="Pdetails"),
]