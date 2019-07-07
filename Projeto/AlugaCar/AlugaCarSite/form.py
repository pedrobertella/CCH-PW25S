import datetime
from django import forms


from .models import Cliente, Aluguel

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