from rest_framework import serializers
from profile_api.models import UserProfile

class UserSerializer(serializers.Serializer):
    """ Serializa un campo para probar nuestro APIView"""

    class Meta:
        model = UserProfile
        fields = ('username','last_name','email')

    
