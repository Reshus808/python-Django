from django.db import models

# Create your models here.

class Student(models.Model):
    Roll = models.IntegerField()
    Name = models.CharField(max_length=50)
    Marks = models.IntegerField()
    Address = models.CharField(max_length=100)

    def str(self):
        return self.Name