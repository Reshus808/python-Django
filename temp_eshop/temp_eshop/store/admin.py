from django.contrib import admin
# Register your models here.
#self

from .models import Category
from .models import Image
from .models import Customer
from .models import Contact
from .models import Orders
from .models import OrderUpdate




admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)



