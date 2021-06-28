from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Manager para perfiles de usuario """
    def create_user(self, email, name, password=None):
        if not email: 
            raise ValueError('El usuario debe tener un email')

        email = self.normalize_email(email) #pasar todo el email a minusculas
        user = self.model(email=email, name=name) #creamos el modelo de usuario
        user.set_password(password) #Le creamos un password
        user.save(using=self._db) #guardamos

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser= True #Este se especifica automaticamente cuando tenemos el permissionsMixin en la otra clase
        user.is_staff=True
        user.save(using=self._db)

# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo de base de datos para usuarios en el sistema """
    email = models.EmailField(max_length=255, unique = True)
    name= models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return f"Nombre corto: {self.name}"

    def __str__(self):
        return self.get_full_name()



