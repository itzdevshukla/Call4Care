
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('team/',views.team,name="team"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('db/',views.report,name="db"),
]