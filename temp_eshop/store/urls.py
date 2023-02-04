from django.urls import path
#self
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('',views.showhome,name='showhome'),
    path('category/<int:cid>/',views.display_by_category,name="display_by_category"),
    path('productview/<int:id>',views.productview,name="productview"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('projecthelp',views.projecthelp,name="projecthelp"),
    path('contact/',views.contact,name="contact"),
    path('search',views.search,name="search"),
    path('checkout/',views.checkout,name="checkout"),
    path('clearcart',views.clearcart,name="clearcart"),
    path('tracker/',views.tracker,name="tracker"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
