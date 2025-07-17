from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request,"dashboard/dashboard.html")

@login_required
def administration_view(request):
    return render(request,"dashboard/admin.html")