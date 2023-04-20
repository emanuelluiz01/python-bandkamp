from django.db import models
from django.contrib.auth.models import AbstractUser

from rest_framework.validators import UniqueValidator


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
