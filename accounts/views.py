from django.shortcuts import render,redirect

from  home.models import Student,Ambulance

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if Student.objects.filter(username = username).exists():

            user = auth.authenticate(request,username = username , password = password)
            if user is not None:
                auth.login(request,user)
                if user.is_superuser:
                    return redirect("administration")
                else:
                    return redirect("dashboard")
        print("Invalid Username or Password")

    return render(request,"accounts/userlogin.html")



def register(request):
    if request.method == "POST":
        print("\n\n")
        user_first_name = request.POST.get("first_name")
        user_last_name = request.POST.get("last_name")
        user_email = request.POST.get("email")
        user_password = request.POST.get("password")
        user_phone_number = request.POST.get("phone_number")
        user_username = request.POST.get("username")

        new_user = Student(
            first_name = user_first_name,
            last_name = user_last_name,
            email = user_email,
            username = user_username,
            phone_number = user_phone_number,   
        )
        new_user.set_password(user_password)
        new_user.save()
        return redirect("login")

    return render(request,"accounts/register.html")



def u_logout(request):
    auth.logout(request)
    return redirect("home")





def ambulance(request):
        if request.method == "POST":  
            User_Ambulance_ID = request.POST.get("AmbulanceId")
            Ambulance_Driver_name = request.POST.get("drivername")
            Ambulance_Type_ = request.POST.get("ambulanceType")
            driver_password = request.POST.get("password")
            Ambulance_Driver_phone_number = request.POST.get("driverphone")
            Ambulance_Vehicle_Number = request.POST.get("vehicleNumber")

            new_ambulance = Ambulance(
                 Ambulance_ID = User_Ambulance_ID,
                 Driver_Name = Ambulance_Driver_name,
                 Driver_Phone_Number = Ambulance_Driver_phone_number,
                 Vehicle_Number = Ambulance_Vehicle_Number,
                 Ambulance_Type = Ambulance_Type_,
                 Driver_Password  = driver_password
            )
            new_ambulance.save()


    
        return render(request,"accounts/ambulance_registration.html")


def hospital(request):
     return render(request,"accounts/hospital_registration.html")



# From here only the read operation is performed
# 1. For User Details
def read(request):
    Users = Student.objects.all().order_by('-id')

    parameters = {
        "Users" : Users
    }

    return render(request,"Details_every/in.html",parameters)

# 2. For Ambulance Details
def ambulance_read(request):
     
     Ambulances = Ambulance.objects.all()


     parameters = {
          "Ambulances" : Ambulances
     }
     return render(request,"Details_every/ambulance_details.html",parameters)



# =========Delete User/Ambulance Details=================

def delete_user(request,user_id):
    User = Student.objects.get(id=user_id)
    User.delete()

    return redirect("read")


def delete_ambulance(request,ambulance_id):
    Ambu = Ambulance.objects.get(id=ambulance_id)
    Ambu.delete()

    return redirect("ambulance_read")



# ======================Edit Details=====================

def edit_user(request,user_id):
    user = Student.objects.get(id=user_id)
    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.phone_number = request.POST.get("phone_number")
        
        user.save()
        return redirect("read")
    
    parameters = {
         "user" : user
    }

    return render(request,"Edit_page/UserEdit.html",parameters)


def edit_ambulance(request,ambulance_id):
    Ambu = Ambulance.objects.get(id = ambulance_id)
    if request.method == "POST":
        Ambu.Ambulance_ID = request.POST.get("AmbulanceId")
        Ambu.Driver_Name = request.POST.get("drivername")
        Ambu.Driver_Phone_Number = request.POST.get("driverphone")
        Ambu.Vehicle_Number = request.POST.get("vehicleNumber")
        Ambu.Ambulance_Type = request.POST.get("ambulanceType")

        Ambu.save()

        return redirect("ambulance_read")
    parameters = {
        "Ambu" : Ambu
    }

    return render(request,"Edit_page/ambulance_edit.html",parameters)