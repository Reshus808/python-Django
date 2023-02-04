from django.contrib import admin
from .models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
   list_display=['Roll','Name','Marks','Address']

#admin.site.register(Student)
admin.site.register(Student,StudentAdmin,)

