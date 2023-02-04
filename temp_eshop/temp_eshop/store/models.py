from django.db import models

# Create your models here.

#creata a Category model
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    #to display title in admin panel
    def __str__(self):
        return self.title


#create a model images
class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images',default="")
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)

    #to display title in admin panel
    def __str__(self):
        return self.title

#create a model Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
    
class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=15,default="")

    def __std__(self):
        return self.email

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
