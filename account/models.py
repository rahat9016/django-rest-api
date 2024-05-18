from typing import Any
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
# Create your models here.

    
    
    
    
class Users(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    password1=models.CharField(max_length=10)
    password2=models.CharField(max_length=10)
    
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    