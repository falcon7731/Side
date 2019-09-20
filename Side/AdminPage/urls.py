from django.urls import path
from . import views
from django.shortcuts import redirect 
from AdminPage import views
urlpatterns = [
    path('' , views.redirect_to_AdminPage),
    path('Login/' , views.Login_view , name='Login'),
    path('ControlPanel/' , views.ControlPanel ,name='ControlPanel')
]
