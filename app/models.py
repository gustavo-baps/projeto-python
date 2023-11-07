from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Admin(models.Model):
    user = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

class Cliente(models.Model):
    nome = models.CharField(max_length=45, blank=False, unique=True)
    sobrenome = models.CharField(max_length=45, blank=False)
    endereco = models.CharField(max_length=255, blank=False, unique=True)
    telefone = models.CharField(max_length=45, blank=False, unique=True)
