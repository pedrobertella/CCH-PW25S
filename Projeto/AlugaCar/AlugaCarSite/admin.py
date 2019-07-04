from django.contrib import admin

from .models import Carro,Cliente,Aluguel

admin.site.register(Carro)

admin.site.register(Cliente)

admin.site.register(Aluguel)
