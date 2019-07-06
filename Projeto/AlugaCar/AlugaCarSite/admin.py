from django.contrib import admin

from .models import Carro,Cliente,Aluguel,Marca,Modelo

admin.site.register(Carro)

admin.site.register(Cliente)

admin.site.register(Aluguel)

admin.site.register(Modelo)

admin.site.register(Marca)