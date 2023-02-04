from django.urls import path
from . import views


urlpatterns = [

    path('', views.home,name="home"),
    path('addrecord', views.addrecord,name="addrecord"),
    path('displayall', views.displayall,name="displayall"),
    path('update', views.update,name="update"),
    path('delete', views.delete,name="delete"),
]