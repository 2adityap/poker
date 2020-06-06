from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from poker.models import Tables
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "startbootstrap-landing-page-gh-pages/index.html", {"message": "Please Log in"})
    context = {
        "user": request.user
    }
    return render(request,"code.html",context)


def loginScreen(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "startbootstrap-landing-page-gh-pageslogin/index.html", {"message": "Please Login Again"})

def logoutScreen(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def load(request):
    return render(request, "register.html")

def registerScreen(request):
    first_name = request.POST["first_name"]
    username = request.POST["username"]
    password = request.POST["password"]
    user = User.objects.create_user(first_name=first_name, username=username, password=password)
    user.save()
    return HttpResponseRedirect(reverse("index"))

def createRoom(request):
    user = request.user
    counter = 3
    tables = Tables(code="{0}".format(counter))
    tables.save()
    tables.players.add(user)
    tables.save()
    context = {
        "tables": tables,
        "players": tables.players.all()
    }
    return render(request, "createRoom.html", context)

def joinRoom(request):
    roomCode = request.POST["roomCode"]
    tables = Tables.objects.all()
    for table in tables:
        if table.code is roomCode:
            user = request.user
            table.players.add(user)
            table.save()
            context = {
                "tables": table,
                "players": table.players.all()
            }
    return render(request, "createRoom.html", context)
