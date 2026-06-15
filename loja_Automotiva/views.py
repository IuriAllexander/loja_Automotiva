import json 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.http import HttpResponse
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm, FabricanteForm, UsuarioForm


def is_staff(user):
    return user.is_authenticated and user.is_staff


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

def categoria_especifica(request, pk):
    categorias = get_object_or_404(Categoria, pk=pk)
    produtos = Produto.objects.filter(categoria=categorias)
    contexto = {'produtos': produtos, 'categoria':categorias}
    return render(request, "loja_Automotiva/pages/categorias.html", contexto)

@user_passes_test(is_staff)
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save()
            messages.success(request, f' Novo produto {produto.nome_produto} cadastrado com sucesso!')
            return redirect('categorias')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = ProdutoForm()

    return render(request, 'loja_Automotiva/pages/cadastro_elementos.html', {
        'form': form,
        'titulo': 'Cadastro de produtos',
    })

@user_passes_test(is_staff)
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            messages.success(request, f' Nova categoria {categoria.nome_categoria} cadastrada com sucesso!')
            return redirect('categorias')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = CategoriaForm()

    return render(request, 'loja_Automotiva/pages/cadastro_elementos.html', {
        'form': form,
        'titulo': 'Cadastro de categoria',
    })

@user_passes_test(is_staff)
def criar_fabricante(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            fabricante = form.save()
            messages.success(request, f' Novo fabricante {fabricante.nome_fabricante} cadastrado com sucesso!')
            return redirect('categorias')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = FabricanteForm()

    return render(request, 'loja_Automotiva/pages/cadastro_elementos.html', {
        'form': form,
        'titulo': 'Cadastro de Fabricante',
    })

@user_passes_test(is_staff)
def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save()
            messages.success(request, f' {usuario.nome_usuario} cadastrado com sucesso!')
            return redirect('categorias')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = ProdutoForm()

    return render(request, 'loja_Automotiva/pages/cadastro_elementos.html', {
        'form': form,
        'titulo': 'Usuario',
    })

@user_passes_test(is_staff)
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Produto "{produto.nome_produto}" atualizado com sucesso!')
            return redirect('produto-detalhe', pk=produto.pk)
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'loja_Automotiva/pages/cadastro_elementos.html', {
        'form': form,
        'titulo': f'Editar: {produto.nome_produto}',
        'editando': True,
    })

@user_passes_test(is_staff)
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        nome = produto.nome_produto
        produto.delete()
        messages.success(request, f'Produto "{nome}" foi removido.')
        return redirect('categorias')

    return render(request, 'loja_Automotiva/pages/excluir.html', {
        'produto': produto,
    })

def produto_page(request, pk):
    """Renderiza a página de produtos."""
    produto =  get_object_or_404(Produto, pk=pk)
    contexto = {'produto': produto}    
    return render(request, 'loja_Automotiva/pages/produto.html', contexto)

def produto_base(request):
    """Renderiza o componente de cards de produtos."""
    produtos = Produto.objects.filter(estoque__gt=1).order_by('preco')[:3]
    contexto = {'produtos': produtos}
    return render(request, 'loja_Automotiva/components/product_card.html', contexto)

@login_required
def perfil_page(request):
    """Renderiza a página de perfil do usuário."""
    return render(request, 'loja_Automotiva/pages/perfil.html')

@login_required
def carrinho_page(request):
    """Renderiza a página do carrinho de compras."""
    return render(request, 'loja_Automotiva/pages/carrinho.html')

def contato_page(request):
    """Renderiza a página de contato."""
    
@login_required
def pagamento_teste_page(request):
    return render(request, 'loja_Automotiva/pages/pagamento_teste.html')
    return render(request, 'loja_Automotiva/pages/contato.html')

@login_required
def cadastro_elementos_page(request):
    return render(request, 'loja_Automotiva/pages/cadastro_elementos.html')

def servicos_page(request):
    return render(request, 'loja_Automotiva/pages/servicos.html')

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
