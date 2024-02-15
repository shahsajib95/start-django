from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .manager import UserManager

# Create your models here.


class CustomUser(AbstractBaseUser):
    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    user_bio = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user_profile_image = models.ImageField(upload_to="profile")
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELD = []
    objects = UserManager()