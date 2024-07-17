from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm # to create form

from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import views as auth_views #for login form create

#to view profile when login only

from django.contrib.auth.decorators import login_required


# Create your views here.
def home(req):
    return render(req, "home.html")

# def login(req):
#     return render(req,"login.html")

def register(req):
    if req.method =='POST':
        name=req.POST['username']
        email=req.POST['email']
        password1=req.POST['password1']
        password2=req.POST['password2']
        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True 
            user.save()
            messages.success(req,"Your Account has been created Successfully")
            return redirect('Login')
        else:
            messages.warning(req,"Password Mismatching")
            return redirect('Register')
    else:
         # form=UserCreationForm()
        form =CreateUserForm()
        return render(req,"register.html",{'form':form})

@login_required
def profile(req):
    return render(req,"profile.html")
   