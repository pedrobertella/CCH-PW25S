from django.shortcuts import render,redirect
from.form import ClienteForm

def cadastro_user(request):
    form = ClienteForm(request.POST or None)
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    if(form.is_valid()):
        print("-----------------------------------------")
        form.save()
        return redirect("")
    return render(request, 'cadastro_user.html', {'form':form})
