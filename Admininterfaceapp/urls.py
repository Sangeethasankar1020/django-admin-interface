from django.contrib import admin
from django.urls import path
from Admininterfaceapp import views
urlpatterns = [
    path('',views.home,name="Home")
]
