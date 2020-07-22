from django.urls import path

from . import views #. represents current directory

urlpatterns = [
    path("", views.index, name = "index"),
    path("createRoom", views.createRoom, name = "createRoom"),
    path("joinRoom", views.joinRoom, name = "joinRoom")
]
