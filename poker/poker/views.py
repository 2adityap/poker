from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from poker.models import Tables, Players
import random
# Create your views here.
def index(request):
    return render(request,"check.html")

def createRoom(request):
    player_name = request.POST["player_name"]
    player = Players(name=player_name)
    player.save()
    counter = random.randrange(1000,100000,1) #increment the counter variable every time a room is created
    tables = Tables(code=counter) #Create new table, with counter being the new room code
    tables.save()
    tables.players.add(player) #add the user who created the table to the table
    tables.save()
    context = {
        "tables": tables,
        "players": tables.players.all()
    }
    return render(request, "createRoom.html", context)

def joinRoom(request):
    roomCode = request.POST["roomCode"] #get the room code
    code = int(roomCode)
    tables = Tables.objects.all() #get all the tables
    for table in tables:
        if (table.code == code) :  #if room code is one of the created table's room code
            player_name = request.POST["player_name"]
            player = Players(name=player_name)
            player.save()
            table.players.add(player) #add the user to the table
            table.save()
            context = {
                "tables": table,
                "players": table.players.all()
            }
            return render(request, "createRoom.html", context)
    return HttpResponseRedirect(reverse("index"))
