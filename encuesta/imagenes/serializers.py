from imagenes.models import Imagen

from rest_framework import serializers

class ImagenSerializer(serializers.Serializer):
    class Meta:
        model = Imagen
        fields= "__all__"

    def create(self, validated_data):
        print(validated_data.get("title"))
        ##Validated_data es un diccionario que contiene todos los fields enviados
        image = Imagen()
        image.title = validated_data.get("title")
   
        image.description = validated_data.get("description")
        image.save()

        return image

        