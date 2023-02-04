from django.contrib import admin

# Register your models here.
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display=['Account','Name','Balance','Email','Mobile','Street','City','State','Country','Password']


#admin.site.register(Customer)
admin.site.register(Customer,CustomerAdmin,)
