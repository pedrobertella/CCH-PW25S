from django.db import models

class Carro(models.Model):
    descricao = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=True)
    valorDia = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    caminhoFoto = models.ImageField(null=True, blank = True,upload_to='AlugaCarSite/static/galeria/carros')
    def __str__(self):
        return self.descricao

    def getfoto(self):
        dir = str(self.caminhoFoto)
        print(dir,"--------------->")
        dir = dir[20:]
        print(dir)
        return dir

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete = models.SET_NULL, null = True)
    carrro = models.ForeignKey(Carro, on_delete=models.CASCADE, null = False)
    dataAlugado = models.DateField()
    diasAluguel = models.IntegerField()
    valorPagar = models.DecimalField(max_digits=10, decimal_places=2)

