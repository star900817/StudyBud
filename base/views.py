from django.shortcuts import render
from django.http import HttpResponse
from . models import Room
from . forms import RoomForm

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
def room(request, pk):
    room = Room.objects.get(id = pk)
    context = {'room': room}

    return render(request, 'base/room.html', context)
# you can use contains functions
def createRoom(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
