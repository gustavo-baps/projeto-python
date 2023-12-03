"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home, painel, dologin, dashboard, logouts, clientes, addcliente, deletecliente, editcliente, equipes, addequipe, deleteequipe, editequipe, mecanicos, addmecanico, deletemecanico, editmecanico, carros, addcarro, deletecarro, editcarro, pecas, addpeca, deletepeca, editpeca, servicos, addservico, deleteservico, editservico, ordens, addordem, deleteordem, editordem, ordem, filtercarros, adm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', painel),
    path('painel/', painel),
    path('dologin/', dologin),
    path('dashboard/', dashboard),
    path('logouts/', logouts),
    path('clientes/', clientes),
    path('addcliente/', addcliente),
    path('deletecliente/<int:cliente_id>/', deletecliente, name='deletecliente'),
    path('editcliente/<int:cliente_id>', editcliente, name = "editcliente"),
    path('equipes/', equipes),
    path('addequipe/', addequipe),
    path('deleteequipe/<int:equipe_id>/', deleteequipe, name="deleteequipe"),
    path('editequipe/<int:equipe_id>', editequipe, name = "editequipe"),
    path('mecanicos/', mecanicos),
    path('addmecanico/', addmecanico),
    path('deletemecanico/<int:mecanico_id>/', deletemecanico, name="deletemecanico"),
    path('editmecanico/<int:mecanico_id>', editmecanico, name = "editmecanico"),
    path('carros/', carros),
    path('addcarro/', addcarro),
    path('deletecarro/<int:carro_id>/', deletecarro, name="deletecarro"),
    path('editcarro/<int:carro_id>', editcarro, name = "editcarro"),
    path('deletemecanico/<int:mecanico_id>/', deletemecanico, name="deletemecanico"),
    path('pecas/', pecas),
    path('addpeca/', addpeca),
    path('deletepeca/<int:peca_id>/', deletepeca, name="deletepeca"),
    path('editpeca/<int:peca_id>', editpeca, name = "editpeca"),
    path('servicos/', servicos),
    path('addservico/', addservico),
    path('deleteservico/<int:servico_id>/', deleteservico, name="deleteservico"),
    path('editservico/<int:servico_id>', editservico, name = "editservico"),
    path('ordens/', ordens),
    path('addordem/', addordem),
    path('deleteordem/<int:ordem_id>/', deleteordem, name="deleteordem"),
    path('editordem/<int:ordem_id>', editordem, name = "editordem"),
    path('ordem/<int:ordem_id>', ordem, name="ordem"),
    path('filtercarros/<int:cliente_id>/', filtercarros, name='filtercarros'),
    path('adm/', adm)
]
