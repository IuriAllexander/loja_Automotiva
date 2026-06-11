from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    descricao = models.TextField(blank=True, null=True)
    codigo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']


class Fabricante(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    pais_origem = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
        ordering = ['nome']


class Produto(models.Model):
    Nome = models.CharField(max_length=150)
    Codigo = models.DecimalField('codigo', max_digits=11, decimal_places=0)
    Peso = models.DecimalField('peso', max_digits=8, decimal_places=2)
    Preco = models.DecimalField('preco', max_digits=10, decimal_places=2)
    Descricao = models.CharField(max_length=300)
    Capa = models.ImageField('Capa', upload_to='capas/', blank=True, null=True)

    fabricante = models.ForeignKey(
        Fabricante,
        on_delete=models.PROTECT,
        related_name='produtos',
        verbose_name='Fabricante',
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='produtos',
        verbose_name='Categoria',
    )

    def __str__(self):
        return self.Nome

    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        ordering = ['Nome']


class Usuario(models.Model):
    Nome = models.CharField(max_length=150)
    Email = models.CharField(max_length=200)
    Telefone = models.DecimalField('telefone', max_digits=15, decimal_places=0)
    Endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.Nome

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['Nome']


class Pedido(models.Model):
    Id_Pedido = models.CharField(
        'id_pedido',
        max_length=11,
        unique=True
    )

    valor_total = models.DecimalField(
        'valor_total',
        max_digits=8,
        decimal_places=2
    )

    forma_pagamento = models.CharField(max_length=150)

    usuario = models.ForeignKey(
        'Usuario',
        on_delete=models.PROTECT,
        related_name='pedidos',
        verbose_name='Usuario',
        null=True,
        blank=True
    )

    produto = models.ManyToManyField(
        'Produto',
        related_name='pedidos',
        verbose_name='Componente',
    )

    def __str__(self):
        return str(self.Id_Pedido)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['Id_Pedido']


class PJ(models.Model):
    Razao_Social = models.CharField(max_length=200)

    Inscricao_Estadual = models.DecimalField(
        'inscricao estadual',
        max_digits=9,
        decimal_places=0
    )

    Cnpj = models.DecimalField(
        'cnpj',
        max_digits=14,
        decimal_places=0
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='PJ',
        verbose_name='Usuario',
    )

    def __str__(self):
        return str(self.Cnpj)


class PF(models.Model):
    Cpf = models.DecimalField(
        'cpf',
        max_digits=11,
        decimal_places=0
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='PF',
        verbose_name='Usuario',
    )

    def __str__(self):
        return str(self.Cpf)