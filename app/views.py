from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import Admin, Cliente, Equipe, Mecanico, Peca, Servico, Carro, Ordem
from .forms import ClienteForm, CarroForm, EquipeForm, MecanicoForm, PecaForm, ServicoForm, OrdemForm
import hashlib
from django.urls import reverse
from django.db.models import Sum

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
        ordens = Ordem.objects.all()
        total_ganhos = sum(ordem.update_venda() for ordem in ordens)
        total_debito = sum(ordem.debito for ordem in Ordem.objects.all())

        context = {'total_ganhos': total_ganhos, 'total_debito': total_debito}
        return render(request, 'dashboard/home.html', context)
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

def editcliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
    else:
        form = ClienteForm(instance = cliente)
    context = {'form': form}
    return render(request, 'clientes/editcliente.html', context)
    
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

def editequipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance = equipe)
        if form.is_valid():
            form.save()
            return redirect('/equipes/')
    else:
        form = EquipeForm(instance = equipe)
    context = {'form': form}
    return render(request, 'equipes/editequipe.html', context)

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

def editmecanico(request, mecanico_id):
    mecanico = get_object_or_404(Mecanico, id=mecanico_id)
    if request.method == 'POST':
        form = MecanicoForm(request.POST, instance = mecanico)
        if form.is_valid():
            form.save()
            return redirect('/mecanicos/')
    else:
        form = MecanicoForm(instance = mecanico)
    context = {'form': form}
    return render(request, 'mecanicos/editmecanico.html', context)

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

def editcarro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance = carro)
        if form.is_valid():
            form.save()
            return redirect('/carros/')
    else:
        form = CarroForm(instance = carro)
    context = {'form': form}
    return render(request, 'carros/editcarro.html', context)

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

def editpeca(request, peca_id):
    peca = get_object_or_404(Peca, id=peca_id)
    if request.method == 'POST':
        form = PecaForm(request.POST, instance = peca)
        if form.is_valid():
            form.save()
            return redirect('/pecas/')
    else:
        form = PecaForm(instance = peca)
    context = {'form': form}
    return render(request, 'pecas/editpeca.html', context)

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

def editservico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance = servico)
        if form.is_valid():
            form.save()
            return redirect('/servicos/')
    else:
        form = ServicoForm(instance = servico)
    context = {'form': form}
    return render(request, 'servicos/editservico.html', context)

def ordens(request):
    ordens = Ordem.objects.all()
    if Cliente.objects.exists() and Carro.objects.exists() and Equipe.objects.exists() and Servico.objects.exists():
        ordensids = request.POST.getlist('ordens_checkbox')
        Ordem.objects.filter(id__in=ordensids).delete()
        return render(request, 'ordens/ordens.html', {'ordens': ordens})
    else:
        context = {'msg': 'Não é possível cadastrar uma ordem sem peças, carros ou serviços', 'class': 'alert-danger'}
        return render(request, 'main.html', context)

def addordem(request):
    form = OrdemForm
    
    if request.method == 'POST':
        form = OrdemForm(request.POST)
        if form.is_valid():
            ordem = form.save()
            ordem.update_totals()
            return redirect('/ordens/')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request, 'ordens/addordem.html', context)
        
def deleteordem(request, ordem_id):
    ordem = get_object_or_404(Ordem, id = ordem_id)
    if request.method == 'POST' and 'ordens_checkbox' in request.POST:
        ordensids = request.POST.getlist('ordens_checkbox')
        Ordem.objects.filter(id__in=ordensids).delete()
    else:
        total_ganhos = ordem.update_venda() if ordem.totalvenda else 0
        total_debito = ordem.debito if ordem.debito else 0

        total_ganhos -= ordem.totalvenda if ordem.totalvenda else 0
        total_debito -= ordem.debito if ordem.debito else 0

        ordem.delete()
    return redirect('/ordens/')

def editordem(request, ordem_id):
    ordem = get_object_or_404(Ordem, id=ordem_id)
    if request.method == 'POST':
        form = OrdemForm(request.POST, instance = ordem)
        if form.is_valid():
            form.save()
            return redirect('/ordens/')
    else:
        form = OrdemForm(instance = ordem)
    context = {'form': form}
    return render(request, 'ordens/editordem.html', context)

def ordem(request, ordem_id):
    ordem = get_object_or_404(Ordem, id = ordem_id)
    preco_total = sum(peca.preco for peca in ordem.pecas.all())
    preco_total_servico = sum(servico.preco for servico in ordem.servicos.all())
    total_venda = preco_total + preco_total_servico
    return render(request, 'ordens/ordem.html', {'ordem':ordem, 'preco_total':preco_total, 'preco_total_servico':preco_total_servico, 'total_venda':total_venda})

def filtercarros(request, cliente_id):
    carros = Carro.objects.filter(cliente_id=cliente_id).values('id', 'modelo', 'placa')
    return JsonResponse(list(carros), safe=False)

def adm(request):
    return render(request, 'adm.html')

    

