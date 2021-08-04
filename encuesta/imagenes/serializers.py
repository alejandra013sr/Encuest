
from drf_extra_fields.fields import Base64ImageField


from imagenes.models import Imagen
from rest_framework import serializers



class ImagenSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = Imagen
        fields= ('title','description','image')
  

    def create(self, validated_data):
      
        ##Validated_data es un diccionario que contiene todos los fields enviados
        image = Imagen()
        image.title = validated_data.get("title")
   
        image.description = validated_data.get("description")
        image.save()

        return image
    





        