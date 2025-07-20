from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Student(User):
    phone_number = models.CharField(max_length=10)
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    


class Ambulance(models.Model):
    Ambulance_type = (
        ("Basic Life Support","Basic Life Support"),
        ("Advanced Life Support","Advanced Life Support"),
        ("ICU Ambulance","ICU Ambulance"),
        ("Oxygen Ambulance","Oxygen Ambulance")

    )
    Ambulance_ID = models.CharField(max_length=55)
    Driver_Name = models.CharField(max_length=50)
    Driver_Phone_Number = models.CharField(max_length=10)
    Vehicle_Number = models.CharField(max_length=25)
    Ambulance_Type = models.CharField(max_length=100 , choices=Ambulance_type)
    Driver_Password = models.CharField(max_length=15)
