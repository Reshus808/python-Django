from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Image
from .models import Category


admin.site.register(Customer)
admin.site.register(Image)
admin.site.register(Category)
