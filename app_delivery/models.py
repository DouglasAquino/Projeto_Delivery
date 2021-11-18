from django.db import models
from django.contrib.auth.models import User



class Funcionario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    nome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=15, blank=True, null=True)
    complemento = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.nome


class Prato(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField()
    valor = models.FloatField()

    def __str__(self):
        return '{} - {}'.format(self.nome, self.valor)

class Pedido(models.Model):
    CHOICES = [
		(1, 'Esperando Restaurante'),
		(2, 'Em Produção'),
		(3, 'Saiu para Entrega'), ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    prato = models.ManyToManyField(Prato)
    status = models.SmallIntegerField(choices=CHOICES, default=1)
    aceitar = models.BooleanField(default=False)
    pronto = models.BooleanField(default=False)
    atendido = models.BooleanField(default=False)
    def __str__(self):
        return self.cliente.nome



