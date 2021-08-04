from django.urls import path

from imagenes.api import ImagenAPI


urlpatterns = [
   path('image/', ImagenAPI.as_view()),
   
  
]