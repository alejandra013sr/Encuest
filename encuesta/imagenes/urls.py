
from django.urls import path

from imagenes.api import ImagenAPI, LikeImageAPI


urlpatterns = [
   path('image/', ImagenAPI.as_view()),
   path('image/detail/', LikeImageAPI.as_view())
   
  
]