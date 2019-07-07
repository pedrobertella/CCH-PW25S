
from django.shortcuts import render,redirect
from .form import ClienteForm,LoginUserForm,AluguelForm
from .models import Cliente,Carro,Aluguel,Marca

def home(request):
    id = request.session.get('login', None)
    if not id or id<0:
        user = Cliente("-1","Login","-1") 
    else:
        user = Cliente.objects.get(id=id)
    carros = Carro.objects.all()
    marcas = Marca.objects.all()
    return render(request, "index.html",{'cliente':user,'carros':carros,'marcas':marcas})

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
                    request.session.set_expiry(0)
                    request.session['login'] = i.id
                    user = Cliente.objects.get(id=i.id)
                    carros = Carro.objects.all()
                    return render(request, "index.html",{'cliente':user,'carros':carros})
    return render(request,'login.html',{'form':form})

def user_page(request):
    iduser=request.session.get('login')
    if iduser < 0 or not iduser:
        return redirect("home")

    user = Cliente.objects.get(id=iduser)
    alu = Aluguel.objects.all()
    alugueis = []
    carros = []
    for i in alu:
        if i.cliente.id == user.id:
            alugueis.append(i)
    return render(request,"user_page.html",{"cliente":user,'alugueis':alugueis,'carros':carros})

def cancelar_aluguel(request,id):
    al = Aluguel.objects.get(id=id)
    car = Carro.objects.get(id= al.carrro.id)
    car.disponivel = True
    car.save() 
    al.delete()
    return redirect("user_page")


def home_deslog(request):
    request.session["login"] =-1
    return redirect("home")

def alugar_confirm(request,id):
    form = AluguelForm(request.POST or None)
    car = Carro.objects.get(id=id)
    if form.is_valid():
        dias = float(request.POST['diasAluguel'])
        cl = Cliente.objects.get(id=request.session.get('login'))
        val = dias * float(car.valorDia)
        alug = Aluguel(cliente=cl,carrro=car,diasAluguel=dias,valorPagar = val)
        alug.save()
        car.disponivel = False
        car.save()
        return redirect("user_page")
    return render(request,"confirm.html",{'carro':car,'form':form})

def alugar(request,id):
    cliente = Cliente.objects.get(request.session.get('login'))
    carro = Carro.objects.get(id=id)
    alug = Aluguel(cliente=cliente,carro=carro)
    alug.save()
    return redirect("user_page")

