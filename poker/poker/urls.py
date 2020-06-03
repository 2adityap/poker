from django.urls import path

from . import views #. represents current directory

urlpatterns = [
    path("", views.index, name = "index"),
    path("login", views.loginScreen, name = "login"),
    path("logout", views.logoutScreen, name = "logout"),
    path("load", views.load, name = "load"),
    path("register", views.registerScreen, name = "register")
]
