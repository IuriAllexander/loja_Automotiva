from .models import Categoria, Produto

def categorias_menu(request):
    return {
        'categorias': Categoria.objects.all()
    }

def produtos_base(request):
     return {
        'produtos': Produto.objects.all()
    }