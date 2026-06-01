from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_to

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = User.objects.filter(username=nome).first()

        if usuario:
            return HttpResponse('já existe um usuario com esse nome')
        
        usuario = User.objects.create_user(
            username = nome, 
            email= email, 
            password =senha)
        usuario.save()
        return HttpResponse('usuario cadastrado com sucesso')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = authenticate(
            username = nome, 
            password = senha)
        
        if usuario:
            login_to(request, usuario)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('email ou senha invalidos')
