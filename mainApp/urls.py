from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('createaccount', views.createaccount),
    path('signin', views.signin),
    path('profile', views.userprofile),
    path('rawfoodkalculator/kalculator', views.kalculator),
    path('logout', views.logout),
]
