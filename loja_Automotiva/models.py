from django.db import models
from django.urls import reverse

# Create your models here.

class Categoria (models.Model):
    nome = models.CharField(max_length=150, unique=True)
    descricao = models.TextField(blank=True, null=True)
    codigo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Meta:
    verbose_name = 'Categoria',
    verbose_name_plural = 'Categorias',
    ordering = ['nome']


class Fabricante(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    pais_origem = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()
    
    def __str__(self):
        return self.nome

class Meta:
    verbose_name = 'Fabricante',
    verbose_name_plural = 'Fabricantes',
    ordering = ['nome']

class Pedido(models.Model):
    Id_Pedido = models.DecimalField('id_pedido', max_digits = 11 ,decimal_places=0)
    valor_total = models.DecimalField('valor_total', max_digits = 8 ,decimal_places=2)
    forma_pagamento = models.CharField(max_length=150)

    def __str__(self):
        return str(self.Id_Pedido)

class Meta:
    verbose_name = 'Id_Pedido',
    verbose_name_plural = 'Id_Pedido',
    ordering = ['Id_Pedido']
    

class Produto(models.Model):
    Nome = models.CharField(max_length=150)
    Codigo = models.DecimalField('codigo', max_digits = 11 ,decimal_places=0)
    Peso = models.DecimalField('peso', max_digits = 8 ,decimal_places=2)
    Preco = models.DecimalField('preco', max_digits = 10 ,decimal_places=2)
    Marca = models.CharField(max_length=150)
    Descricao = models.CharField(max_length=300)

    def __str__(self):
        return self.Nome

class Meta:
    verbose_name = 'Componente',
    verbose_name_plural = 'Componentes',
    ordering = ['nome']

class Usuario(models.Model):
    Nome = models.CharField(max_length=150)
    Email = models.CharField(max_length=200)
    Telefone = models.DecimalField('telefone', max_digits=15, decimal_places=0)
    Endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.Nome

class Meta:
    verbose_name = 'Usuario',
    verbose_name_plural = 'Usuarios',
    ordering = ['nome']
    
class PJ(models.Model):
    Razao_Social = models.CharField(max_length=200)
    Inscricao_Estadual = models.DecimalField('inscricao estadual', max_digits=9, decimal_places=0)
    Cnpj =  models.DecimalField('cnpj', max_digits=14, decimal_places=0)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='PJ',
        verbose_name='Usuario',
    )

class PF(models.Model):
    Cpf =  models.DecimalField('cpf', max_digits=11, decimal_places=0)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='PF',
        verbose_name='Usuario',
    )
