from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

    
class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    email_address = models.EmailField( max_length=50, unique=True)
    username = models.CharField(max_length=75, unique=True)
    full_name = models.CharField(max_length=100)
    profile_image_url = models.URLField(blank=True)
    bio = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = CustomUserManager()
    