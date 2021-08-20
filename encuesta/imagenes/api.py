


from imagenes.models import Imagen, LikeImage
from imagenes.serializers import ImagenSerializer, LikeImageSerializer

from profile_api.models import UserProfile
from profile_api.serializers import ListUserSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

class ImagenAPI(APIView):

    def get(self,request):
        imagenes = Imagen.objects.all()
        imagenes_serializer = ImagenSerializer(imagenes,many=True)
        return Response(imagenes_serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        imagen_serializer = ImagenSerializer(data=request.data)
        user = UserProfile.objects.filter(email=request.data["email"]).first()

        if imagen_serializer.is_valid():
            

            validated_data = imagen_serializer.validated_data
    
            #Convertir y guardar el modelo
            new_like_image= LikeImage()
            new_like_image.save()

            imagen = Imagen(**validated_data)
            imagen.user= user
            imagen.like_image=new_like_image
            
            imagen.save()

            imagen_serializer=ImagenSerializer(imagen)
      
            
            return Response(imagen_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'No se pudo guardar correctamente'},status=status.HTTP_400_BAD_REQUEST)



class ImageUserAPI(APIView):
    def get(self,request):
        try:
            token = request.headers.get('Authorization')
            
            token=token.strip('Bearer ')
            token = Token.objects.filter(key=token).first()
            
            user_image=token.user

            imagenes = Imagen.objects.filter(user=user_image)
            imagenes_serializer = ImagenSerializer(imagenes, many=True)
            
            return Response({'imagenes':imagenes_serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'mensaje':'El usuario no tiene imagenes'})

    def delete(self,request):
        try:
            image = Imagen.objects.filter(id=request.data["id"]).first()
            
            image.image.delete(save=True)
            like_image=LikeImage.objects.filter(id=image.like_image.id).first()
            like_image.delete()

            image.delete()

            return Response({"mensaje":"Imagen borrada"}, status=status.HTTP_200_OK)
        except:
            return Response({"Error":"La imagen no existe"}, status=status.HTTP_400_BAD_REQUEST)
        


class LikeImageAPI(APIView):

    def get(self,request,pk, format=None):
  
        try:
            image = Imagen.objects.get(pk=pk)
            image_serializer= ImagenSerializer(image)
            return Response({'Imagen':image_serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'Error':'No existe'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,format=None):
        try: 
            #Recojo los datos (pk se pasa por la url y el email por el body)
            token = request.headers.get('Authorization')
            token=token.strip('Bearer ')
           
            token = Token.objects.filter(key=token).first()
            
            if token:
                
                user = token.user
  
            image = Imagen.objects.get(pk=request.data["id"])
            like=LikeImage.objects.get(id=image.like_image.id)
           
            aux = LikeImage.objects.filter(id=like.id,like_image__id=user.id)
           
            #Serializo el usuario en general
            user_serializer=ListUserSerializer(user)
            #Cambio datos(agregar a la lista si el usuario no ha reaccionado)
            if not(aux):
                like.cant_likes +=1
                like.like_image.add(user)
                like.save()

                like_serializer= LikeImageSerializer(like)
                
            
                return Response({'Imagen':like_serializer.data,'Usuario':user_serializer.data,'mensaje':'El usuario dio like'}, status=status.HTTP_200_OK)
            #Cambio datos(elimino de la lista si el usuario ya reacciono y quito su like)
            else:
                like.cant_likes-=1
                like.like_image.remove(user.id)
                like.save()
                like_serializer= LikeImageSerializer(like)
                return Response({'Image':like_serializer.data,'Usuario':user_serializer.data,'mensaje':'el usuario quito el like'}, status=status.HTTP_302_FOUND)
        except:
            return Response({'Error':'No existe'}, status=status.HTTP_400_BAD_REQUEST)

    

    



