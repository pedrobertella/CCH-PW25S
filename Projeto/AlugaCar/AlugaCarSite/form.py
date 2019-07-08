import datetime
from django import forms


from .models import Cliente, Aluguel, Marca, Modelo, Carro

class PesquisaForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = {"dataAlugado"}        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = {"email","senha","nome"}

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = Cliente
        widgets = {
        "senha": forms.PasswordInput(),
        }
        fields = {"email","senha"}

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        widgets ={
            'dataAlugado': forms.DateTimeInput()
        }
        fields = {"diasAluguel","dataAlugado"}

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'
    
class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'