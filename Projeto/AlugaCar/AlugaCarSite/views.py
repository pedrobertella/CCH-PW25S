from datetime import datetime,date
from django.shortcuts import render,redirect
from .form import ClienteForm,LoginUserForm,AluguelForm,PesquisaForm
from .models import Cliente,Carro,Aluguel,Marca

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
    if not id or id<0:
        user = Cliente("-1","Login","-1") 
    else:
        user = Cliente.objects.get(id=id)
    carros = Carro.objects.all()
    marcas = Marca.objects.all()
    if (form.is_valid()):
        data = request.POST['dataAlugado']
        d = datetime.strptime(data, '%Y-%m-%d').date()
        alugueis = Aluguel.objects.all()
        cars =[]
        for i in carros:
            disponivel = True
            for j in alugueis:
                if(j.carrro.id == i.id):
                    p=0
                    while( p < j.diasAluguel):
                        prox = date.fromordinal(j.dataAlugado.toordinal()+p)
                        if(prox == d):
                            disponivel=False
                        p+=1
            if(disponivel):
                cars.append(i)
        return render(request,"index.html",{'cliente':user,'carros':cars,'marcas':marcas,"form":form}) 
        
    return render(request, "index.html",{'cliente':user,'carros':carros,'marcas':marcas,"form":form})

def cadastro_user(request):
    form = ClienteForm(request.POST or None)
    if(form.is_valid()):
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
        user_id =request.session.get('login')
        if(not user_id is None):
            if user_id > 0:
                cl = Cliente.objects.get(id=user_id)
                dias = float(request.POST['diasAluguel'])
                data = request.POST['dataAlugado']
                d = datetime.strptime(data, '%Y-%m-%d').date()
                val = dias * float(car.valorDia)
                alug = Aluguel(cliente=cl,carrro=car,diasAluguel=dias,valorPagar = val,dataAlugado = d)
                alug.save()
                #car.disponivel = False
                car.save()
                return redirect("user_page")
            else:
                return redirect("login_user")
        else:
                return redirect("login_user")

    return render(request,"confirm.html",{'carro':car,'form':form})

def alugar(request,id):
    cliente = Cliente.objects.get(request.session.get('login'))
    carro = Carro.objects.get(id=id)
    alug = Aluguel(cliente=cliente,carro=carro)
    alug.save()
    return redirect("user_page")

