import json 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .models import Produto





def home_page(request):
    """Renderiza a página inicial com produtos em destaque."""
    produtos = Produto.objects.filter(estoque__gt=1).order_by('preco')[:3]
    contexto = {'produtos': produtos}
    return render(request, 'loja_Automotiva/home/index.html', contexto)


def categorias_page(request):
    """Renderiza a página de categorias com os produtos disponíveis."""
    produtos = Produto.objects.all()
    contexto = {'produtos': produtos}
    return render(request, "loja_Automotiva/pages/categorias.html", contexto)

def login_page(request):
    return render(request, 'loja_Automotiva/pages/login.html')


def cadastro_page(request):
    return render(request, 'loja_Automotiva/pages/cadastro.html')





def produto_base(request):
    """Renderiza o componente de cards de produtos."""
    produtos = Produto.objects.filter(estoque__gt=1).order_by('preco')[:3]
    contexto = {'produtos': produtos}
    return render(request, 'loja_Automotiva/components/product_card.html', contexto)




def adicionar_produto(request):
    if request == 'GET':
        return render(request, 'loja_Automotiva/pages/adicionar.html')



def login_page(request):
    """Renderiza a página de login."""
    return render(request, 'loja_Automotiva/pages/login.html')


def cadastro_page(request):
    """Renderiza a página de cadastro."""
    return render(request, 'loja_Automotiva/pages/cadastro.html')


def perfil_page(request):
    """Renderiza a página de perfil do usuário."""
    
    return render(request, 'loja_Automotiva/pages/perfil.html')


def pagina_produto(request):
    """Renderiza a página de detalhes do produto."""
    
    pass


def produto_page(request):
    """Renderiza a página de produtos."""
    
    return render(request, 'loja_Automotiva/pages/produto.html')


def carrinho_page(request):
    """Renderiza a página do carrinho de compras."""
    return render(request, 'loja_Automotiva/pages/carrinho.html')


def contato_page(request):
    """Renderiza a página de contato."""
    
    return render(request, 'loja_Automotiva/pages/contato.html')





#Chatbot
@csrf_exempt
def responder_chatbot(request):
    """Processa mensagens do chatbot e retorna uma resposta em JSON."""
    
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


def login_teste_page(request):
    return render(request, 'loja_Automotiva/pages/login_teste.html')

def cadastro_teste_page(request):
    return render(request, 'loja_Automotiva/pages/cadastro_teste.html')

def servicos_page(request):
    return render(request, 'loja_Automotiva/pages/servicos.html')

def pagamento_teste_page(request):
    return render(request, 'loja_Automotiva/pages/pagamento_teste.html')