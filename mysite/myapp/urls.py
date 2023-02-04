from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('add/', views.add),
    path('edit/<int:id>', views.editData),
    path('delete/<int:id>', views.delete),
    path('', views.show),
]