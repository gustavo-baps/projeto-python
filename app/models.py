from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Admin(models.Model):
    user = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)


