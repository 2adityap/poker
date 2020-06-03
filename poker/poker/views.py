from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "startbootstrap-landing-page-gh-pages\index.html", {"message": "Please Log in"})
    context = {
        "user": request.user
    }
    return render(request, "code.html",context)


def loginScreen(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "startbootstrap-landing-page-gh-pageslogin\index.html", {"message": "Please Login Again"})

def logoutScreen(request):
    logout(request)
    return render(request, "startbootstrap-landing-page-gh-pageslogin\index.html", {"message": "Logged out User"})

def registerScreen(request):
    first_name = request.GET["first_name"]
    username = request.POST["username"]
    password = request.POST["password"]
    user = User.objects.create_user(first_name=first_name, username=username, password=password)
    user.save()
    return HttpResponseRedirect(reverse("index"))
