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
    

class Personalizacao(models.Model):
    tipo = models.CharField(max_length=150)
    tamanho = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)

    def __str__(self):
        return self.tipo

class Meta:
    verbose_name = 'Personalizacao',
    verbose_name_plural = 'Personalizações',
    ordering = ['nome']



class Loja_Automotiva(models.Model):
    nome = models.CharField('Loja', max_length=150, unique=True)
    endereco = models.CharField('Endereço', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='Loja_Automotiva',
        verbose_name='Categoria',
    )

    fabricante = models.ForeignKey(
        Fabricante,
        on_delete=models.PROTECT,
        related_name='Loja_Automotiva',
        verbose_name='Fabricante',
    )

    personalizacao = models.ForeignKey(
        Personalizacao,
        on_delete=models.PROTECT,
        related_name='Loja_Automotiva',
        verbose_name='Personalizacao',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('Loja_Automotiva', kwargs={'pk': self.pk})

class Meta:
    verbose_name = 'Loja_Automotiva',
    verbose_name_plural = 'Loja_Automotivas',
    ordering = ['nome']
