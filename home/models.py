from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    


class Ambulance(models.Model):
    Ambulance_ID = models.CharField(max_length=55)
    Driver_Name = models.CharField(max_length=50)
    Driver_Phone_Number = models.IntegerField(max_length=10)
    Vehicle_Number = models.CharField(max_length=25)
    Ambulance_Type = models.CharField(max_length=100)
    Driver_Password = models.CharField(max_length=15)

