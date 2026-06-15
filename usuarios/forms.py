from django import forms
from django.contrib.auth import get_user_model
User= get_user_model()

class CadastroUsuarioForm(forms.modelForm):
    password = forms.CharField(label="Senha",zzz)

