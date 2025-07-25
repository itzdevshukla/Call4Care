from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from home.models import Student
import requests

api_key = "AIzaSyB8tg_h-W4i8xOycDuqR6jzSCBomWwKj6g"

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

@login_required
def ask_ai(request):
    if request.method == "POST":
        query = request.POST.get("query")
        response = generate_response(query)
        parameters = {
            'response':response
        }
        return render(request,'dashboard/ask_ai.html',parameters)
    return render(request,"dashboard/ask_ai.html")


def generate_response(query):

    prompt = (
        "You are Dr. Aarav Mehta, the Chief Medical Officer of Call4Care. "
        "Tum ek professional doctor ho jo accident, emergency aur health-related queries me madad karta hai. "
        "Apne aap ko kabhi AI ya chatbot na kehna, tum ek real doctor ki tarah baat karoge. "
        "Jab bhi numbered points ya steps batao, unhe hamesha alag line par likho, "
        "jaise:\n1. Pehla step\n2. Dusra step\n3. Teesra step.\n"
        "Sab steps clearly line break ke saath dikhne chahiye, ek hi line me chipak ke nahi. "
        "Sirf jitna poocha gaya hai, utna hi jawab do.\n\n"
        "Now, user ka sawaal hai: " + query
    )




    api = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

    url = f"{api}?key={api_key}"

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    if "candidates" in data:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"API Error: {data}"