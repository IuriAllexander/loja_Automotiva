from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Produto


def home(request):
    produtos = Produto.objects.filter(estoque__gt=1).order_by('preco')[:3]
    contexto = {'produtos': produtos}
    return render(request, "index.html", contexto)

def paginaCategoria(request):
    produtos = Produto.objects.filter(estoque__gt=1)
    busca = request.GET.get('find','')
    if busca:
        produtos = Produtos.filter(nome_produto__icontains=busca)
    contexto = {'produtos':produtos, 'busca':busca}
    return render(request, "pages/categorias.html", contexto)

def paginaProduto(request):
    pass