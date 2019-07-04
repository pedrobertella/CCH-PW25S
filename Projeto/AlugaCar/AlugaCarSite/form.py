from django import forms

from .models import Cliente

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