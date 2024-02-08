from django.db import models


# Create your models here.
class Student(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    file = models.ImageField(null=True, blank=True)
    
class Car(models.Model):
    #id = models.AutoField()
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)
    
    def __str__(self) -> str:
        return self.car_name 


