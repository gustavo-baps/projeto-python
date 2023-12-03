from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Admin(models.Model):
    user = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

class Peca(models.Model):
    nome = models.CharField(max_length=45, unique=True, blank=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=45, unique=True, blank=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=45, blank=False, unique=True)
    sobrenome = models.CharField(max_length=45, blank=False)
    endereco = models.CharField(max_length=255, blank=False, unique=True)
    telefone = models.CharField(max_length=45, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=45, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Mecanico(models.Model):
    nome = models.CharField(max_length=45, blank=False, unique=True)
    sobrenome = models.CharField(max_length=45, blank=False)
    endereco = models.CharField(max_length=100, blank=False, unique=True)
    especialidade = models.CharField(max_length=100, blank=False)
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)

class Carro(models.Model):  
    marca = models.CharField(max_length=45, blank=False)
    modelo = models.CharField(max_length=45, blank=False)
    placa = models.CharField(max_length=45, blank=False, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo + " " + self.placa

class Ordem(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    carro = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    defeito = models.CharField(max_length=255, blank=False)
    servicos = models.ManyToManyField(Servico, blank=True)
    pecas = models.ManyToManyField(Peca, blank=True)
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    data = models.DateField(blank=False)
    dataconclusao = models.DateField(blank=False)
    totalvenda = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    debito = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    concluida = models.BooleanField(default=False)

    def update_totals(self):
        total_peca_cost = sum(peca.preco for peca in self.pecas.all())
        self.debito = total_peca_cost

        self.save()
    def update_venda(self):
        preco_total = sum(peca.preco for peca in self.pecas.all())
        preco_total_servico = sum(servico.preco for servico in self.servicos.all())
        self.totalvenda = preco_total + preco_total_servico
        self.save()
        return self.totalvenda