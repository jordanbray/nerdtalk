from django.contrib.auth import login as dlogin, logout as dlogout, authenticate
from django.shortcuts import redirect
from django_auth_ldap.backend import LDAPBackend
from menu import Menu

from nerdtalk.views import render
from .forms import LogInForm

# Create your views here.
def login(request):
    login_form = LogInForm()
    if request.method == "POST":
        login_form = LogInForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user != None and user.is_authenticated():
                dlogin(request, user)
                return redirect('/')
    return render("login.html", request, {"login_form": login_form })

def logout(request):
    username = request.user.username
    dlogout(request)
    return redirect('/')

def home(request):
    Menu.process("main", request)
    return render("auth.html", request)

