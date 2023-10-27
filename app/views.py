from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')

def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senhas não coincidem'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado'
        data['class'] = 'alert-success'
    return render(request, 'create.html', data)

def painel(request):
    return render(request, 'painel.html')

def dologin(request):
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    data = {}
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválidos'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)
    
def dashboard(request):
    return render(request, 'dashboard/home.html')

def logouts(request):
    logout(request)
    return redirect('/painel/')

