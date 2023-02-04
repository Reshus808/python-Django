from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', views.showhome,name='showhome'),
    path('signup', views.signup,name='signup'),
    path('aboutus', views.aboutus,name='aboutus'),
    path('contactus', views.contactus,name='contactus'),
    path('projecthelp', views.projecthelp,name='projecthelp'),
    path('display_by_category', views.display_by_category,name='display_by_category'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)