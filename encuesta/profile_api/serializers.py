from rest_framework import serializers
from profile_api.models import UserProfile

class UserSerializer(serializers.Serializer):
    """ Serializa un campo para probar nuestro APIView"""
    id = serializers.ReadOnlyField()

    email = serializers.EmailField()
    name= serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        ##Validated_data es un diccionario que contiene todos los fields enviados
       
        user = UserProfile()
        user.name = validated_data.get("name")
        user.email = validated_data.get("email")
        user.set_password(validated_data.get("password"))
        user.save()

        return user

    def validate_email(self,data):
        users = UserProfile.objects.filter(email=data)
        if len(users) != 0:
            raise serializers.ValidationError("Este email de usuario ya existe, ingrese uno nuevo")
        else:
            return data
    
