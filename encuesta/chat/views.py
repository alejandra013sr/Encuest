from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def message(request):
    return render(request, 'index.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name,
        'username': request.user.name,
        'email': request.user.email
    })