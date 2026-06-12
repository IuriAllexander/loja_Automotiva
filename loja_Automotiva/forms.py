from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Produto, Categoria, Fabricante, Usuario, Pedido

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'codigo_produto',
            'nome_produto',
            'preco',
            'estoque',
            'peso',
            'descricao',
            'foto',
        ]
    widgets = {
        'codigo_produto': forms.NumberInput(attrs={'class': 'form-control', 'max':11}),
        'nome_produto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Volante'}),
        'estoque': forms.NumberInput(attrs={'class': 'form-control', 'min':0}),
        'peso': forms.NumberInput(attrs={'class': 'form-control'}),
        'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        'foto': forms.FileInput (attrs={'class': 'form-control'}) ,
    }
