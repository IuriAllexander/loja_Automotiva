from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, f'Bem-vindo(a), {user.username}!')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/cadastro.html', {'form': form})