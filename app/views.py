from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Admin, Cliente, Carro, Equipe, Mecanico, Peca, Servico, Ordem
from .forms import ClienteForm, EquipeForm, MecanicoForm, CarroForm, PecaForm, ServicoForm, OrdemForm
import hashlib
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'painel.html')

#user: admin, senha: 123

def painel(request):
    return render(request, 'painel.html')

def dologin(request):
    user = request.POST.get('user')
    password = request.POST.get('password')

    try:
        admin = Admin.objects.get(user=user)

        if admin.password == hashlib.md5(password.encode()).hexdigest():
            request.session['id'] = admin.id
            print(admin.id)
            print(admin.user)
            print(admin.password)
            return redirect('/dashboard/')
    except Admin.DoesNotExist:
        print('erro')
    data = {
        'msg':'Usuário ou senha inválidos',
        'class': 'alert-danger'
    }
    return render(request, 'painel.html', data)
    
def dashboard(request):
    if is_authenticated(request):
        return render(request, 'dashboard/home.html')
    else:
        return redirect('/painel/')
    
def logouts(request):
    logout(request)
    return redirect('/painel/')

def is_authenticated(request):
    if 'id' in request.session:
        try:
            admin = Admin.objects.get(id=request.session['id'])
            return True
        except Admin.DoesNotExist:
            return False
    return False

def clientes(request):
    clientes = Cliente.objects.all()
    for cliente in clientes:
        cliente.numero_carros = Carro.objects.filter(cliente=cliente).count()

    return render(request, 'clientes/clientes.html', {'clientes': clientes})

def addcliente(request):
    form = ClienteForm
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
    context = {'form':form}
    return render(request, 'clientes/addcliente.html', context)
        
def deletecliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id = cliente_id)
    cliente.delete()
    return redirect('/clientes/')

    
def equipes(request):
    equipes = Equipe.objects.all()
    return render(request, 'equipes/equipes.html', {'equipes': equipes})

def addequipe(request):
    form = EquipeForm
    
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/equipes/')
    context = {'form':form}
    return render(request, 'equipes/addequipe.html', context)
        
def deleteequipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id = equipe_id)
    equipe.delete()
    return redirect('/equipes/')

def mecanicos(request):
    mecanicos = Mecanico.objects.all()
    if Equipe.objects.exists():
        return render(request, 'mecanicos/mecanicos.html', {'mecanicos': mecanicos})
    else:
        context = {'msg': 'Não é possível cadastrar um mecânico sem equipes', 'class': 'alert-danger'}
        return render(request, 'main.html', context)

def addmecanico(request):
    form = MecanicoForm
    
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mecanicos/')
    context = {'form':form}
    return render(request, 'mecanicos/addmecanico.html', context)
        
def deletemecanico(request, mecanico_id):
    mecanico = get_object_or_404(Mecanico, id = mecanico_id)
    mecanico.delete()
    return redirect('/mecanicos/')

def carros(request):
    carros = Carro.objects.all()
    if Cliente.objects.exists() and Equipe.objects.exists():
        return render(request, 'carros/carros.html', {'carros': carros})
    else:
        context = {'msg': 'Não é possível cadastrar um carro sem clientes ou equipes', 'class': 'alert-danger'}
        return render(request, 'main.html', context)

def addcarro(request):
    form = CarroForm
    
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/carros/')
    context = {'form':form}
    return render(request, 'carros/addcarro.html', context)
        
def deletecarro(request, carro_id):
    carro = get_object_or_404(Carro, id = carro_id)
    carro.delete()
    return redirect('/carros/')

def pecas(request):
    pecas = Peca.objects.all()
    return render(request, 'pecas/pecas.html', {'pecas': pecas})

def addpeca(request):
    form = PecaForm
    
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pecas/')
    context = {'form':form}
    return render(request, 'pecas/addpeca.html', context)
        
def deletepeca(request, peca_id):
    peca = get_object_or_404(Peca, id = peca_id)
    peca.delete()
    return redirect('/pecas/')

def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/servicos.html', {'servicos': servicos})

def addservico(request):
    form = ServicoForm
    
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/servicos/')
    context = {'form':form}
    return render(request, 'servicos/addservico.html', context)
        
def deleteservico(request, servico_id):
    servico = get_object_or_404(Servico, id = servico_id)
    servico.delete()
    return redirect('/servicos/')

def ordens(request):
    ordens = Ordem.objects.all()
    if Cliente.objects.exists() and Equipe.objects.exists() and Servico.objects.exists():
        return render(request, 'ordens/ordens.html', {'ordens': ordens})
    else:
        context = {'msg': 'Não é possível cadastrar um carro sem clientes ou equipes', 'class': 'alert-danger'}
        return render(request, 'main.html', context)

def addordem(request):
    form = OrdemForm
    
    if request.method == 'POST':
        form = OrdemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ordens/')
    context = {'form':form}
    return render(request, 'ordens/addordem.html', context)
        
def deleteordem(request, ordem_id):
    ordem = get_object_or_404(Ordem, id = ordem_id)
    ordem.delete()
    return redirect('/ordens/')

def ordem(request, ordem_id):
    ordem = get_object_or_404(Ordem, id = ordem_id)
    preco_total = sum(peca.preco for peca in ordem.pecas.all())
    preco_total_servico = sum(servico.preco for servico in ordem.servicos.all())
    total_venda = preco_total + preco_total_servico
    return render(request, 'ordens/ordem.html', {'ordem':ordem, 'preco_total':preco_total, 'preco_total_servico':preco_total_servico, 'total_venda':total_venda})