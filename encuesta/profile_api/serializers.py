from decimal import Context
from django.contrib.auth import authenticate

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
        fields = ('id','name','email')

    def to_representation(self,instance):
        return{
            'id': instance['id'],
            'name': instance['name'],
            'email': instance['email'],
        }

class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


    def validate(self, data):

        email = data.get('email')
        password = data.get('password')
        if email and password:

            user = authenticate(request=self.context.get('request'), email=email,password=password)

            if not user:
                print("No existe usuario")
                msg=("No se encontro un usuario con esas características")
                raise serializers.ValidationError(msg, code='authorization')
            else:
                print("Si existe usuario")
                msg=("Si existe")

            data['user']=user
        return data 

    
   
    """
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(email=data['email'], password=data['password'])
     
        if not user:
            print("no existe")
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return user
"""
