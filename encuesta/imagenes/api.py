from rest_framework import response
from rest_framework.serializers import Serializer
from imagenes.models import Imagen
from imagenes.serializers import ImagenSerializer

from profile_api.models import UserProfile

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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
            imagen = Imagen(**validated_data)
            imagen.user= user
            imagen.save()

            imagen_serializer=ImagenSerializer(imagen)
      
            
            return Response(imagen_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'No se pudo guardar correctamente'},status=status.HTTP_400_BAD_REQUEST)


    def get_object(self,pk):
        image = get_object_or_404(Imagen,pk)
        return image

    def delete(self,request,pk):
        image = self.get_object(pk)
        image.image.delete(save=True)
        image.delete()
        return Response({"mensaje":"Imagen borrada"}, status=status.HTTP_200_OKs)
