from django.db import models
from django.urls import reverse

# ======================================= MODELS ======================================

# Model Categoria: representa categorias de produtos
class Categoria(models.Model):
    codigo_categoria = models.AutoField('categoria', primary_key=True, default=0)
    nome_categoria = models.CharField('nome', max_length=50, unique=True, blank=False, null=True)
    descricao = models.TextField('descricao', blank=True, null=True)

    def __str__(self):
        return self.nome_categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome_categoria']

# Model Fabricante: representa fabricantes de produtos
class Fabricante(models.Model):
    nome_fabricante = models.CharField('nome', max_length=150, unique=True, blank=False, null=True)
    cnpj = models.CharField(max_length=14, unique=True, blank=False, null=True)
    endereco_fabricante = models.CharField(max_length=200, blank=True, null=True)
    telefone_fabricante = models.CharField('telefone', max_length=11, blank=False, null=True)
    email_fabricante = models.EmailField('email', max_length=200, unique=True, blank=False, null=True)
    website = models.URLField(blank=True)
    pais_origem = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome_fabricante

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
        ordering = ['nome_fabricante']


# Model Usuario: representa usuários do sistema
class Usuario(models.Model):
    nome_usuario = models.CharField('nome', max_length=150, unique=True, blank=False, null=False, default='Anonimo')
    cpf = models.CharField('cpf', max_length=11, unique=True, blank=False, null=True)
    email_usuario = models.EmailField('email', max_length=200, unique=True, blank=False, null=True)
    telefone_usuario = models.CharField('telefone', max_length=11, blank=False, null=True)
    endereco_usuario = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome_usuario

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nome_usuario']


# Model Produto: representa produtos
class Produto(models.Model):
    codigo_produto = models.CharField('codigo', primary_key=True, max_length=11, default=0)
    nome_produto = models.CharField(max_length=150)
    preco = models.DecimalField('preco', max_digits=10, decimal_places=2, blank=False, null=False, default=0)
    estoque = models.PositiveIntegerField('estoque', blank=False, null=False, default=0)
    peso = models.DecimalField('peso', max_digits=8, decimal_places=2, blank=False, null=True)
    descricao = models.CharField('descricao', max_length=300, blank=False, null=True)
    foto = models.ImageField('Capa', upload_to='capas/', blank=True, null=True)

    # Relacionamento com fabricante
    fabricante = models.ForeignKey(
        Fabricante,
        default=0,
        on_delete=models.PROTECT,
        related_name='produtos',
        verbose_name='Fabricante',
    )

    # Relacionamento com categoria
    categoria = models.ForeignKey(
        Categoria,
        default=0,
        on_delete=models.PROTECT,
        related_name='produtos',
        verbose_name='Categoria',
    )

    def __str__(self):
        return self.nome_produto

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome_produto']


class FormaPagamento(models.TextChoices):
    CARTAO_CREDITO = 'CC', 'Cartão de Crédito'
    CARTAO_DEBITO = 'CD', 'Cartão de Débito'
    BOLETO = 'BL', 'Boleto'
    PIX = 'PX', 'Pix'

# Model Pedido: representa pedidos realizados por usuários
class Pedido(models.Model):
    id_pedido = models.AutoField('id_pedido', primary_key=True, default=0)
    valor_total = models.DecimalField('valor_total', max_digits=8, decimal_places=2)
    data_pedido = models.DateField(auto_now=True)
    quantidade = models.PositiveIntegerField(blank=False, default=1)
    
    # Forma de pagamento
    forma_pagamento = models.CharField(
        max_length=2,
        blank=False,
        choices=FormaPagamento.choices,
        default= FormaPagamento.CARTAO_CREDITO
        )

    # Relacionamento com o usuário que fez o pedido
    usuario = models.ForeignKey(
        Usuario,
        default=0,
        related_name='pedidos',
        on_delete=models.PROTECT,
        verbose_name='Usuario',
    )

    # Produtos incluídos no pedido (Many-to-Many)
    produto = models.ManyToManyField(
        Produto,
        related_name='pedidos',
        verbose_name='Produto',
    )

    def __str__(self):
        return str(self.id_pedido)

    class Meta:
        verbose_name ='Pedido'
        verbose_name_plural ='Pedidos'
        ordering = ['id_pedido']