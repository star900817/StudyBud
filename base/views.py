from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]

# Create your views here.
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
def room(request, pk):
    return render(request, 'base/room.html')
