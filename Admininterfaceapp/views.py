from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # to create form







# Create your views here.
def home(req):
    return render(req, "home.html")

def login(req):
    return render(req,"login.html")

def register(req):
    form=UserCreationForm()
    return render(req,"register.html",{'form':form})