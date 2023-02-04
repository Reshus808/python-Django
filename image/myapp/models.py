from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

def __str__(self):
    return self.first_name


class Category(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()


def __str__(self):
    return self.title


class Image(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to ='image',default="")
    price = models.IntegerField(default=0)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)


def __str__(self):
    return self.title
