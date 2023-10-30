from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Admin
import hashlib

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')



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
