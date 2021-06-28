from django.core.exceptions import AppRegistryNotReady
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profile_api import serializers
# Create your views here.

class HelloApiView(APIView):
    """Api View de prueba """

    serializer_class = serializers.HelloSerializer

    def get(self,request, format=None):
        """ Retornar lista de características """
        an_apiview=['Usamos metodos http como funciones','Otro elemento de la lista']


        return Response({'message':'Hello world','an_api':an_apiview})

    def post(self,request):
        """ Crea un mensaje con nuestro  nombre """
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
