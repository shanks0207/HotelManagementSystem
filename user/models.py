from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length = 200, default = 'user', null = True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 300)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']