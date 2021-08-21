from django.db import models

from profile_api.models import UserProfile

# Create your models here.


class LikeImage(models.Model):
    like_image=models.ManyToManyField(UserProfile, null=True)
    cant_likes= models.IntegerField(default=0)
    op=models.BooleanField(default=False)
    


    def __str__(self):
        return (self.title)

class Imagen(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True )
    title = models.CharField(max_length=300, blank=True,null=True)
    description = models.CharField(max_length=400, blank=True,null=True)
    image= models.ImageField(null=True,default="",upload_to='fotos/')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    like_image = models.ForeignKey(LikeImage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (self.title)