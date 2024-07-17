from django.contrib import admin
from django.urls import path
from Admininterfaceapp import views
from django.contrib.auth import views as auth_views #for login form create
urlpatterns = [
    path('',views.home,name="Home"),
    # path('login/',views.login,name="Login"),
    path("login/",auth_views.LoginView.as_view(template_name='login.html'),name="Login"),
    path("logout/",auth_views.LogoutView.as_view(template_name='logout.html'),name="Logout"),
    path('register/',views.register,name="Register"),
    path('profile/',views.profile ,name="Profile"),
]
