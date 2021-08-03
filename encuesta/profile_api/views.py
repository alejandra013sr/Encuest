from django.contrib.sessions.models import Session #Esta clase maneja las sesiones
from datetime import datetime

import rest_framework
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.views import APIView

from .models import UserProfile
from .serializers import loginSerializer, UserTokenSerializer

class Login(ObtainAuthToken):



    def post(self,request,*args,**kwargs):
      
        login_serializer = loginSerializer(data=request.data,context = {'request':request}) ##Este es un serializador que trae el obtain auth token, en la documentación aparece que solo tiene los campos de username y contraseña

        if login_serializer.is_valid():
            """
            email = login_serializer.validated_data['email']
            
            user = UserProfile.objects.get(email=email)
            user_serializer = UserTokenSerializer(user)
            """
            user = login_serializer.validated_data['user']
           
            user_serializer = UserTokenSerializer(user)
                    
            
            if user.is_active:
                
                token,created = Token.objects.get_or_create(user=user)
              
                if created: ##Si el token no ha sido creado
                    return Response({'token':token.key,
                                    'user':user_serializer.data,
                                    'message': 'Inicio de sesión exitoso con token creado'
                                    }, 
                    
                                 status= status.HTTP_201_CREATED)
                
                else: ##Si el token  ya fue creado
                    ##Para solo tener una sesion abierta (si se inicia en otro lado se cierra el resto)
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):# se asigna el id al que corresponde la sesión del usuario
                                session.delete()

                    token.delete() ##Borramos el token
                    token= Token.objects.create(user=user)
                    return Response({'token':token.key,
                                    'user':user_serializer.data,
                                    'message': 'Inicio de sesión exitoso con token creado'
                                    }, 
                    
                                 status= status.HTTP_201_CREATED)

            else:
                return Response({'error':'Este usuario no puede iniciar sesión'}, status=status.HTTP_401_UNAUTHORIZED)
        else: 
            return Response({'error':'Email o contraseña incorrectos.'},
                            status=status.HTTP_400_BAD_REQUEST)
            

        return Response({'message':'Hola desde response'}, status = status.HTTP_200_OK)

class Logout(APIView):

    def post(self,request, *args,**kwargs):
        try: 
            token = request.headers.get('Authorization')
            token=token.strip('Bearer ')
            print(token)
            token = Token.objects.filter(key=token).first()
            
            if token:
                
                user = token.user
                
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):# se asigna el id al que corresponde la sesión del usuario
                            session.delete()
                
                token.delete()
                session_message="Sesiones de usuario eliminadas."
                token_message="Token eliminado."
                    
                return Response({'token_message': token_message,'session_message': session_message},
                            status=status.HTTP_200_OK)
        
            return Response({'error':'No se ha encontrado un usuario con estas credenciales'}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'error': 'No se ha encontrado un token en la petición'}, status=status.HTTP_409_CONFLICT)
