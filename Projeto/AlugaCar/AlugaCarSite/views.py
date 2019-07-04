from django.shortcuts import render,redirect
from.form import ClienteForm,LoginUserForm
from.models import Cliente

def cadastro_user(request):
    form = ClienteForm(request.POST or None)
    if(form.is_valid()):
        print("Salvando usario")
        form.save()
        return redirect("")
    return render(request, 'cadastro_user.html', {'form':form})
def login_user(request):
    form = LoginUserForm(request.POST or None)
    if(form.is_valid()):
        users = Cliente.objects.all()
        email = request.POST['email']
        senha = request.POST['senha']
        for i in users:
            if(i.email == email):
                if(i.senha == senha):
                    print("Usuario logado")
                    redirect("home")
    return render(request,'login.html',{'form':form})
