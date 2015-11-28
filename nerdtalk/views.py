from django.shortcuts import render as drender

def render(name, request, data={}):
    data["request"] = request
    return drender(request, name, data)

# Create your views here.

def home(request):
    return render("home.html", request)

