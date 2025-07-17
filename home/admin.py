from django.contrib import admin

# Register your models here.
from .models import Student,Ambulance

admin.site.register(Student)

admin.site.register(Ambulance)