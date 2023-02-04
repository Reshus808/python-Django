from django.db import models

# Create your models here.
class Customer(models.Model):
    Account = models.IntegerField()
    Name = models.CharField(max_length=50)
    Balance = models.IntegerField()
    Mobile = models.IntegerField(max_length=100)
    Email = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Password = models.IntegerField(max_length=100)

    def str(self):
        return self.Account