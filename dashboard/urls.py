from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('administration/',views.administration_view,name="administration"),
    path('ask_ai/',views.ask_ai,name="ask_ai")
]