
from drf_extra_fields.fields import Base64ImageField


from imagenes.models import Imagen, LikeImage
from rest_framework import serializers

from profile_api.models import UserProfile



class ImagenSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = Imagen
        fields= ('title','description','image','user','id')
  
    #No se esta llamando porque no se esta ejecutando un save() en el serializer que esta en api
    def create(self, validated_data):
        ##Validated_data es un diccionario que contiene todos los fields enviados
        image = Imagen()
        image.title = validated_data.get("title")
   
        image.description = validated_data.get("description")
        
        image.save()

        return image
    
class LikeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeImage
        fields = ('cant_likes','id')

    





        