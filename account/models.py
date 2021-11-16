from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=128)
    uni_num = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    card = models.ImageField(upload_to = "account/", blank=True, null=True)