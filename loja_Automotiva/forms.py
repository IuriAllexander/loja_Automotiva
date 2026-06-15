from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Produto, Categoria, Fabricante, Usuario

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome_produto',
            'codigo_produto',
            'preco',
            'estoque',
            'peso',
            'descricao',
            'foto',
            'fabricante',
            'categoria',

        ]
         
    widgets = {
        'nome_produto': forms.TextInput(attrs = {'placeholder': 'Ex.: Volante'}),
        'codigo_produto': forms.NumberInput(attrs = {'max':11, 'placeholder': 'Ex.: 123XXXXX'}),
        'preco': forms.NumberInput(attrs = {'step':'0.01', 'min':0}),
        'estoque': forms.NumberInput(attrs = {'min':0}),
        'peso': forms.NumberInput(),
        'descricao': forms.Textarea(),
        'foto': forms.FileInput () ,
        'fabricante': forms.Select (), 
        'categoria': forms.Select (),
    }

    labels = {
        'codigo_produto': 'Código do produto',
        'nome_produto': 'Nome',
        'preco': 'Preço',
        'estoque': 'Estoque',
        'peso': 'Peso',
        'descricao': 'Descrição',
        'foto':'Foto',
        'fabricante':'Fabricante',
        'categoria':'Categoria',
    }

def clean_codigo_produto(self):
    if len(codigo_produto) not in (11):
        raise ValidationError('Codigo do produto deve ter 11 dígitos.')
    if not codigo_produto.isdigit():
        raise ValidationError('Deve conter apenas números')
    return codigo_produto

def clean_preco(self):
    preco = self.cleaned_data['preco']
    if preco <= 0:
        raise ValidationError('O preço deve ser maior que zero.')
    return preco


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nome_categoria',
            'descricao',
        ]
    widgets = {
        'nome_categoria': forms.TextInput(attrs = {'placeholder': 'Ex.: Motor'}),
        'descricao': forms.Textarea(),
    }

    labels = {
        'nome_categoria': 'Nome',
        'descricao': 'Descrição',
    }

def clean_nome_categoria(self):
    if nome_categoria.isdigit():
        raise ValidationError('Deve conter apenas letras')
    return codigo_produto


class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = [
            'nome_fabricante',
            'cnpj',
            'endereco_fabricante',
            'telefone_fabricante',
            'email_fabricante',
            'website',
            'pais_origem',

        ]
    widgets = {
        
        'cnpj': forms.NumberInput(attrs = {'max':14, 'placeholder': 'Ex.: 123.XXX.XX'}),
        'nome_fabricante': forms.TextInput(),
        'endereco_fabricante': forms.NumberInput(),
        'telefone_fabricante': forms.TelInput(),
        'email_fabricante': forms.EmailInput(),
        'website': forms.URLInput(),
        'pais_origem': forms.TextInput(attrs = {'placeholder': 'Ex.: Brasil'}), 
    }

    labels = {
        'cnpj': 'CNPJ do Fabricante',
        'nome_fabricante': 'Nome',
        'endereco_fabricante': 'Endereço',
        'telefone_fabricante': 'Telefone',
        'email_fabricante': 'Email',
        'website': 'URL do site',
        'pais_origem':'País de origem',
    }

def clean_cnpj(self):
    cnpj = self.cleaned_data['cnpj'].replace('-', '').replace('/', '').replace('.','')
    if len(cnpj) not in (14):
        raise ValidationError('CNPJ deve ter 14 dígitos.')
    if not cnpj.isdigit():
        raise ValidationError('Deve conter apenas números')
    return cnpj

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome_usuario',
            'cpf',
            'endereco_usuario',
            'telefone_usuario',
            'email_usuario',
        ]
    widgets = {
        
        'cpf': forms.NumberInput(attrs = {'max':11, 'placeholder': 'Ex.: 123.XXX.XX'}),
        'nome_usuario': forms.TextInput(),
        'endereco_usuario': forms.NumberInput(),
        'telefone_usuario': forms.TelInput(),
        'email_usuario': forms.EmailInput(),
        }

    labels = {
        'cpf': 'CPF',
        'nome_usuariO': 'Nome',
        'endereco_usuario': 'Endereço',
        'telefone_usuario': 'Telefone',
        'email_usuario': 'Email',
    }

def clean_cpf(self):
    cpf = self.cleaned_data['cpf'].replace('-', '').replace('.','')
    if len(cpf) not in (11):
        raise ValidationError('CPF deve conter 11 dígitos.')
    if not cpf.isdigit():
        raise ValidationError('Deve conter apenas números')
    return cpf