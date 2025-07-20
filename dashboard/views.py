from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from home.models import Student

# Create your views here.
@login_required
def dashboard(request):
    student = Student.objects.get(id = request.user.id)
    parameters = {
        "student": student
    }
    return render(request,"dashboard/dashboard.html",parameters)

@login_required
def administration_view(request):
    return render(request,"dashboard/admin.html")