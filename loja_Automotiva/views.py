from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Produto


def home(request):
    produtos = Produto.objects.filter(estoque__gt=1).order_by('preco')[:3]
    contexto = {'produtos': produtos}
    return render(request, "index.html", contexto)