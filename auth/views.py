from nerdtalk.views import render
from django.contrib.auth import login as dlogin, authenticate
from django.shortcuts import redirect
from .forms import LogInForm

# Create your views here.

def login(request):
    user = authenticate(username="testa", password="johnldap")
    login_form = LogInForm()
    if request.method == "POST":
        login_form = LogInForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user != None and user.is_authenticated():
                return redirect('/')
    return render("login.html", request, {"login_form": login_form })

def home(request):
    return render("auth.html", request)

