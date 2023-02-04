from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('display_rec',views.display_rec,name='display_rec'),
    path('check',views.check,name='check'),
]