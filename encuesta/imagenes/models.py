from django.db import models

from profile_api.models import UserProfile

# Create your models here.
class Imagen(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True )
    title = models.CharField(max_length=300, blank=True,null=True)
    description = models.CharField(max_length=400, blank=True,null=True)
    image= models.ImageField(null=True,default="",upload_to='fotos/')


    def __str__(self):
        return (self.title)
