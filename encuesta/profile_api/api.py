##Este archivo es como si fuera un views.py como cuando trabajamos con django normal
##Este archivo va a recibir los datos y los manda al serializador

from profile_api.models import UserProfile
from rest_framework.response import Response


from .serializers import UserSerializer, ListUserSerializer
from rest_framework.views import APIView
from rest_framework import status


class UserAPI(APIView): 

    def get(self,request):
        users = UserProfile.objects.all().values('id','name','email','password')
        users_serializer = ListUserSerializer(users, many = True)
        return Response(users_serializer.data)

    def post(self,request):
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

