from datetime import datetime, date
from django.shortcuts import render, redirect
from .form import ClienteForm, LoginUserForm, AluguelForm, PesquisaForm, MarcaForm, ModeloForm, CarroForm
from .models import Cliente, Carro, Aluguel, Marca, Modelo

'''def home(request):
    id = request.session.get('login', None)
    if not id or id<0:
        user = Cliente("-1","Login","-1")
    else:
        user = Cliente.objects.get(id=id)
    carros = Carro.objects.all()
    marcas = Marca.objects.all()

    alugueis = Aluguel.objects.all()
    horarios =[]
    for i in carros:
        hor = car_hor(i.carro.id)
        for j in alugueis:
            if(j.carro.id == i.id):
                hor.addHorario(j.dataAlugado)
                p=0
                while p<j.diasAluguel:
                    prox = date.fromordinal(j.dataAlugado.toordinal()+p)
                    hor.addHorario(prox)
                    p+=1
        horarios.append(hor)

    return render(request, "index.html",{'cliente':user,'carros':carros,'marcas':marcas,'horarios':horarios})
'''


def home(request):
    form = PesquisaForm(request.POST or None)
    id = request.session.get('login', None)
    if not id or id < 0:
        user = Cliente("-1", "Login", "-1")
    else:
        user = Cliente.objects.get(id=id)
    carros = Carro.objects.all()
    marcas = Marca.objects.all()
    if (form.is_valid()):
        data = request.POST['dataAlugado']
        d = datetime.strptime(data, '%Y-%m-%d').date()
        alugueis = Aluguel.objects.all()
        cars = []
        for i in carros:
            disponivel = True
            for j in alugueis:
                if(j.carrro.id == i.id):
                    p = 0
                    while(p < j.diasAluguel):
                        prox = date.fromordinal(j.dataAlugado.toordinal()+p)
                        if(prox == d):
                            disponivel = False
                        p += 1
            if(disponivel):
                cars.append(i)
        return render(request, "index.html", {'cliente': user, 'carros': cars, 'marcas': marcas, "form": form})

    return render(request, "index.html", {'cliente': user, 'carros': carros, 'marcas': marcas, "form": form})


def cadastro_user(request):
    form = ClienteForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect("home")
    return render(request, 'cadastro_user.html', {'form': form})

def new_marca(request):
    form = MarcaForm(request.POST or None)
    ma = Marca.objects.all()
    if(form.is_valid()):
        form.save()
        return redirect("admin_page")
    return render(request, 'new_marca.html', {'form': form, 'marcas':ma})

def new_modelo(request):
    form = ModeloForm(request.POST or None)
    mo = Modelo.objects.all()
    if(form.is_valid()):
        form.save()
        return redirect("admin_page")
    return render(request, 'new_modelo.html', {'form': form, 'modelos':mo})

def new_carro(request):
    form = CarroForm(request.POST or None, request.FILES or None)
    if(form.is_valid()):
        form.save()
        return redirect("admin_page")
    return render(request, 'carro.html', {'form': form})


def alt_carro(request, id):
    car = Carro.objects.get(id=id)
    form = CarroForm(request.POST or None, request.FILES or None, instance=car)
    if(form.is_valid()):
        form.save()
        return redirect("admin_page")
    return render(request, 'carro.html', {'form': form, 'carro': car})

def login_user(request):
    form = LoginUserForm(request.POST or None)
    if(form.is_valid()):
        users = Cliente.objects.all()
        email = request.POST['email']
        senha = request.POST['senha']
        for i in users:
            if(i.email == email):
                if(i.senha == senha):
                    if email == 'admin' and senha == '0000':
                        request.session.set_expiry(0)
                        request.session['login'] = i.id
                        user = Cliente.objects.get(id=i.id)
                        users = Cliente.objects.all()
                        carros = Carro.objects.all()
                        alugueis = Aluguel.objects.all()
                        return render(request, "admin_page.html", {'cliente': user, 'carros': carros, 'usuarios':users, 'alugueis' : alugueis})
                    request.session.set_expiry(0)
                    request.session['login'] = i.id
                    user = Cliente.objects.get(id=i.id)
                    carros = Carro.objects.all()
                    return render(request, "index.html", {'cliente': user, 'carros': carros})
    return render(request, 'login.html', {'form': form})

def admin_page(request):
    iduser = request.session.get('login')
    if iduser < 0 or not iduser:
        return redirect("home")
    user = Cliente.objects.get(id=iduser)
    users = Cliente.objects.all()
    carros = Carro.objects.all()
    alugueis = Aluguel.objects.all()
    return render(request, "admin_page.html", {'cliente': user, 'carros': carros, 'usuarios':users, 'alugueis' : alugueis})


def user_page(request):
    iduser = request.session.get('login')
    if iduser < 0 or not iduser:
        return redirect("home")

    user = Cliente.objects.get(id=iduser)
    alu = Aluguel.objects.all()
    alugueis = []
    carros = []
    for i in alu:
        if i.cliente.id == user.id:
            alugueis.append(i)
    return render(request, "user_page.html", {"cliente": user, 'alugueis': alugueis, 'carros': carros})


def cancelar_aluguel(request, id):
    al = Aluguel.objects.get(id=id)
    car = Carro.objects.get(id=al.carrro.id)
    car.disponivel = True
    car.save()
    al.delete()
    return redirect("user_page")

def cancelar_aluguel_admin(request, id):
    al = Aluguel.objects.get(id=id)
    car = Carro.objects.get(id=al.carrro.id)
    car.disponivel = True
    car.save()
    al.delete()
    return redirect("admin_page")

def apaga_user_admin(request, id):
    user = Cliente.objects.get(id=id)
    if user.nome!='admin':
        user.delete()
    return redirect("admin_page")

def apaga_marca(request, id):
    marca = Marca.objects.get(id=id)
    marca.delete()
    return redirect("new_marca")

def apaga_modelo(request, id):
    modelo = Modelo.objects.get(id=id)
    modelo.delete()
    return redirect("new_modelo")

def apaga_carro(request, id):
    car = Carro.objects.get(id=id)
    car.delete()
    return redirect("admin_page")

def home_deslog(request):
    request.session["login"] = -1
    return redirect("home")


def alugar_confirm(request, id):
    form = AluguelForm(request.POST or None)
    car = Carro.objects.get(id=id)
    if form.is_valid():
        user_id = request.session.get('login')
        if(not user_id is None):
            if user_id > 0:
                cl = Cliente.objects.get(id=user_id)
                dias = float(request.POST['diasAluguel'])
                data = request.POST['dataAlugado']
                d = datetime.strptime(data, '%Y-%m-%d').date()
                val = dias * float(car.valorDia)
                alug = Aluguel(cliente=cl, carrro=car,
                               diasAluguel=dias, valorPagar=val, dataAlugado=d)
                alug.save()
                car.disponivel = False
                car.save()
                return redirect("user_page")
            else:
                return redirect("login_user")
        else:
            return redirect("login_user")

    return render(request, "confirm.html", {'carro': car, 'form': form})


def alugar(request, id):
    cliente = Cliente.objects.get(request.session.get('login'))
    carro = Carro.objects.get(id=id)
    alug = Aluguel(cliente=cliente, carro=carro)
    alug.save()
    return redirect("user_page")
