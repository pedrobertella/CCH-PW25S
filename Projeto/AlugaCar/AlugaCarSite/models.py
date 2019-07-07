from django.db import models
class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Carro(models.Model):
    descricao = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=True)
    valorDia = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo,on_delete=models.CASCADE)
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
    '''def __init__(self,cl,car,alugue,dias,valor):
        self.cliente=cl
        self.carro=car
        self.dataAlugado = alugue
        self.diasAluguel=dias
        self.valorPagar = valor'''
    cliente = models.ForeignKey(Cliente,on_delete = models.SET_NULL, null = True)
    carrro = models.ForeignKey(Carro, on_delete=models.CASCADE, null = False)
    dataAlugado = models.DateField(auto_now=False, auto_now_add=False,null=True)
    diasAluguel = models.IntegerField(null=True)
    valorPagar = models.DecimalField(max_digits=10, decimal_places=2)

