from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Produto


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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




#Chatbot
@csrf_exempt
def responder_chatbot(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body)
            mensagem_usuario = dados.get("mensagem", "").lower().strip()

            if "olá" in mensagem_usuario or "oi" in mensagem_usuario:
                resposta_bot = "Olá! Como posso te ajudar hoje?"
            elif "ajuda" in mensagem_usuario:
                resposta_bot = "Você pode me perguntar sobre nossos serviços ou horários."
            else:
                resposta_bot = "Desculpe, ainda estou aprendendo e não entendi sua mensagem."

            return JsonResponse({"resposta": resposta_bot})
            
        except json.JSONDecodeError:
            return JsonResponse({"erro": "Dados inválidos"}, status=400)
            
    return JsonResponse({"erro": "Método não permitido"}, status=405)
def produtoBase(request):
    produtos = Produto.objects.filter(estoque__gt=1).order_by('preco')[:3]
    contexto = {'produtos': produtos}
    return render(request, 'components/product_card.html', contexto)
