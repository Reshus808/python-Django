from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('display_rec',views.display_rec,name='display_rec'),
    path('deletedisplay',views.deletedisplay,name='deletedisplay'),
    path('deleterecord/<int:id>',views.deleterecord,name='deleterecord'),
    path('updatedisplay',views.updatedisplay,name='updatedisplay'),
    path('editrecord/<int:id>',views.editrecord,name='editrecord'),
    path('updaterecord/<int:id>',views.updaterecord,name='updaterecord'),
    path('check',views.check,name='check'),
]



 