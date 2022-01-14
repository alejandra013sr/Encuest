from django.urls import path

from profile_api.api import UserAPI

from .views import message, room

urlpatterns = [
   path('', message, name="message"),
   path('<str:room_name>/', room, name='room'),
   
]