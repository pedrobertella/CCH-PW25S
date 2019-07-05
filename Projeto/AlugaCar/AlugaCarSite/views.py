from django.shortcuts import render,redirect
from .form import ClienteForm,LoginUserForm
from .models import Cliente

def home(request):
    id = request.session.get('login', None)
    if not id:
        user = Cliente("-1","Login","-1") 
    else:
        user = Cliente.objects.get(id=id)
    return render(request, "index.html",{'cliente':user})

def cadastro_user(request):
    form = ClienteForm(request.POST or None)
    if(form.is_valid()):
        print("Salvando usario")
        form.save()
        return redirect("home")
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
                    print(i)
                    request.session['login'] = i.id
                    return redirect('home')
    return render(request,'login.html',{'form':form})
