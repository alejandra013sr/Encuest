from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.views import ObtainAuthToken


from .models import UserProfile
from .serializers import loginSerializer

class Login(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
      
        login_serializer = loginSerializer(data=request.data,context = {'request':request}) ##Este es un serializador que trae el obtain auth token, en la documentación aparece que solo tiene los campos de username y contraseña

        if login_serializer.is_valid():
            print("paso la validación")

        return Response({'message':'Hola desde response'}, status = status.HTTP_200_OK)


