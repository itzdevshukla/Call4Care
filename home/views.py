from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,"home/index.html")
def team(request):
    return render(request , "home/team.html")
def services(request):
    return render(request,"home/services.html")
def report(request):
    return render(request,"home/db.html")
def about(request):
    return render(request,"home/about.html")