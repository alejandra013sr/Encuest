from django.core.exceptions import AppRegistryNotReady
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework import status
from profile_api.serializers import UserSerializer
# Create your views here.

class HelloApiView(APIView):
    """Api View de prueba """

    serializer_class = UserSerializer

    def get(self,request, format=None):
        username = request.GET.get('username')

        try:
            user_token = Token.objects.get(
                user= UserSerializer().Meta.model.objects.filter(username=username).first()
            )

            return Response({'token': user_token.key})
        except:
            return Response({'error':'Credenciales enviadas incorrectas'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        """ Crea un mensaje con nuestro  nombre """
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
