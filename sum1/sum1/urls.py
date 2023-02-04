"""sum1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login,name="login.html"),
    path('home', views.home,name="home.html"),
    path('Sum', views.Sum,name="Sum.html"),
    path('calculate', views.calculate,name="calculate.html"),
    path('Product', views.Product,name="Product.html"),
    path('calculate1', views.calculate1,name="calculate1.html"),
    path('Difference', views.Difference,name="Difference.html"),
    path('calculate2', views.calculate2,name="calculate2.html"),
    path('Average', views.Average,name="Average.html"),
    path('calculate3', views.calculate3,name="calculate3.html"),
    path('Contact', views.Contact,name="Contact.html"),
    path('help', views.help,name="help.html"),
    path('chk_login', views.chk_login,name="chk_login.html"),


    
    


]
