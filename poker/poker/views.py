from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from poker.models import Tables
# Create your views here.
counter = 0
def index(request):
    if not request.user.is_authenticated:
        return render(request, "startbootstrap-landing-page-gh-pages/index.html", {"message": "Please Log in"})
    context = {
        "user": request.user
    }
    return render(request,"check.html",context)

def loginScreen(request):
    username = request.POST["username"] #get the username from the HTML page
    password = request.POST["password"] #get the password from the HTML page
    user = authenticate(request, username=username, password=password) #check if the user is in the Users database
    if user is not None: #if this user is authenticated, log them in
        login(request, user)
        return HttpResponseRedirect(reverse("index")) #go back to main page
    else:
        return render(request, "startbootstrap-landing-page-gh-pageslogin/index.html", {"message": "Please Login Again"}) #if not authenticated, do it again

def logoutScreen(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def load(request):
    return render(request, "register.html") #purpose of this function is to load the register page

def registerScreen(request):
    first_name = request.POST["first_name"] #get the first name from the HTML page
    username = request.POST["username"] #get the username from the HTML page
    password = request.POST["password"] #get the password from the HTML page
    user = User.objects.create_user(first_name=first_name, username=username, password=password) #create a new user from the information given
    user.save()
    return HttpResponseRedirect(reverse("index")) #go back to the main page to log in again

def createRoom(request):
    user = request.user  #get the current user logged in
    global counter
    counter = counter + 1 #increment the counter variable every time a room is created
    tables = Tables(code="{0}".format(counter)) #Create new table, with counter being the new room code
    tables.save()
    tables.players.add(user) #add the user who created the table to the table
    tables.save()
    context = {
        "tables": tables,
        "players": tables.players.all()
    }
    return render(request, "createRoom.html", context)

def joinRoom(request):
    roomCode = request.POST["roomCode"] #get the room code
    tables = Tables.objects.all() #get all the tables
    for table in tables:
        if table.code is roomCode:  #if room code is one of the created table's room code
            user = request.user #get the current user logged in
            table.players.add(user) #add the user to the table
            table.save()
            context = {
                "tables": table,
                "players": table.players.all()
            }
    return render(request, "createRoom.html", context)
