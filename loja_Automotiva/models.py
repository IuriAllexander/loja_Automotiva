from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=150, unique=True, null=True, blank=True)
    descricao = models.TextField(blank=True, null=True)
    codigo = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']


# Model Fabricante: representa fabricantes de produtos
class Fabricante(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    pais_origem = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()

    def __str__(self):
        return self.nome
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
        ordering = ['nome']

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


# ==========================================
# MODEL PRODUTO (REFEITO DO ZERO - LIMPO)
# ==========================================
class Produto(models.Model):
    # 1. Chave Primária (Identificador único do produto no banco)
    codigo_produto = models.CharField('Código do Produto', primary_key=True, max_length=11, default='0')
    
    # 2. Campos de Informação do Produto
    nome_produto = models.CharField('Nome do Produto', max_length=150)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2, default=0.00)
    estoque = models.PositiveIntegerField('Estoque', default=0)
    peso = models.DecimalField('Peso (kg)', max_digits=8, decimal_places=2, null=True, blank=True)
    descricao = models.CharField('Descrição', max_length=300, null=True, blank=True)
    foto = models.ImageField('Foto da Capa', upload_to='capas/', blank=True, null=True)

    # 3. Relacionamento com Fabricante (Mantendo o que o resto do sistema espera)
    fabricante = models.ForeignKey(
        'Fabricante',
        default=1,
        on_delete=models.PROTECT,
        related_name='produtos',
        verbose_name='Fabricante',
    )

    # 4. Relacionamento com Categoria (Mantendo o que o resto do sistema espera)
    categoria = models.ForeignKey(
        'Categoria',
        default=1,
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
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        ordering = ['Nome']

        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome_produto']


class FormaPagamento(models.TextChoices):
    CARTAO_CREDITO = 'CC', 'Cartão de Crédito'
    CARTAO_DEBITO = 'CD', 'Cartão de Débito'
    BOLETO = 'BL', 'Boleto'
    PIX = 'PX', 'Pix'

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

    # Relacionamento com o usuário que fez o pedido
    usuario = models.ForeignKey(
        Usuario,
        default=0,
        related_name='perfil_pj',
        on_delete=models.PROTECT,
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
