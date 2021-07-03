from django.urls import path

from profile_api.api import UserAPI

urlpatterns = [
   path('users/', UserAPI.as_view()),
  
]