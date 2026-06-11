from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Produto


def home(request):
    produtos = Produto.objects.filter(estoque__gt=1).order_by('preco')[:3]
    contexto = {'produtos': produtos}
    return render(request, 'home/index.html', contexto)

def login_page(request):
    return render(request, 'pages/login.html')

def cadastro_page(request):
    return render(request, 'pages/cadastro.html')

def perfil_page(request):
    return render(request, 'pages/perfil.html')

def paginaCategoria(request):
    produtos = Produto.objects.filter(estoque__gt=1)
    busca = request.GET.get('find', '')
    if busca:
        produtos = Produto.objects.filter(nome_produto__icontains=busca)
    contexto = {'produtos': produtos, 'busca': busca}
    return render(request, "pages/categorias.html", contexto)

def categorias_page(request):
    return render(request, 'pages/categorias.html')

def paginaProduto(request):
    pass

def produtos_page(request):
    return render(request, 'pages/produtos.html')

def carrinho_page(request):
    return render(request, 'pages/carrinho.html')

def contato_page(request):
    return render(request, 'pages/contato.html')