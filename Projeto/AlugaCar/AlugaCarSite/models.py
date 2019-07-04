from django.db import models

class Carro(models.Model):
    desricao = models.CharField(max_length=50)

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete = models.SET_NULL, null = True)
    carrro = models.ForeignKey(Carro, on_delete=models.CASCADE, null = False)