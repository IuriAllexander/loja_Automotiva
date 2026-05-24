from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return HttpResponse('<h1> Oi, visitantes<h1> \
     <p>Sejam bem vindos a Loja de Veiculos')


@login_required(login_url='/auth/login/')
def carrinho(request):
    return HttpResponse('carrinho')