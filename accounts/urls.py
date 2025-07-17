from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('login/',views.userlogin,name="login"),
    path('register/',views.register,name="register"),
    path('Registered_Users/',views.read,name="read"),
    path('Register_Ambulance/',views.ambulance,name="ambulance"),
    path('Registered_Ambulance/',views.ambulance_read,name="ambulance_read"),
    path('Register_Hospital/',views.hospital,name="hospital"),
    path("delete_User/<int:user_id>",views.delete_user,name="delete_User"),
    path("delete_ambulance/<int:ambulance_id>",views.delete_ambulance,name="delete_ambulance"),
    path('edit_user/<int:user_id>',views.edit_user,name="edit_User"),
    path('edit_ambulance/<int:ambulance_id>',views.edit_ambulance,name="edit_ambulance"),
    path('logout/',views.u_logout,name="logout")
]