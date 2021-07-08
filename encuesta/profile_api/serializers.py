from django.contrib.auth.models import User
from rest_framework import serializers
from profile_api.models import UserProfile

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile()
        fields = ('name','email')

class UserSerializer(serializers.ModelSerializer):
    """ Serializa un campo para probar nuestro APIView"""
    class Meta:
        model = UserProfile
        fields = "__all__"

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
    
#Se usara para listar todos los usuarios solicitados por get
class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

    def to_representation(self,instance):
        return{
            'id': instance['id'],
            'name': instance['name'],
            'email': instance['email'],
            'password': instance['password']
        }