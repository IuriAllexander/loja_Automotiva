from django.db import models
from django.urls import reverse

# Create your models here.

class Categoria (models.Model):
    nome = models.CharField(max_length=150, unique=True)
    descricao = models.TextField(blank=True, null=True)
    codigo = models.CharField(max_length=50, unique=True)

class Meta:
    verbose_name = 'Categoria',
    verbose_name_plural = 'Categorias',
    ordering = ['nome']


    def __str__(self):
        return self.nome

class Fabricante(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    pais_origem = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()

class Meta:
    verbose_name = 'Fabricante',
    verbose_name_plural = 'Fabricantes',
    ordering = ['nome']


    def __str__(self):
        return self.nome

        


class Personalização(models.Model):
    rodas = models.CharField(max_length=150)
    escapamento = models.TextField(max_length=150)
    espelho = models.CharField(max_length=150)

class Meta:
    verbose_name = 'Personalização',
    verbose_name_plural = 'Personalizações',
    ordering = ['nome']


    def __str__(self):
        return self.rodas


class loja_Automotiva(models.Model):
    nome = models.CharField('Loja', max_length=150, unique=True)
    endereco = models.CharField('Endereço', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)



    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='loja_Automotiva',
        verbose_name='Categoria',
    )

    fabricante = models.ForeignKey(
        Fabricante,
        on_delete=models.PROTECT,
        related_name='loja_Automotiva',
        verbose_name='Fabricante',
    )

    personalização = models.ForeignKey(
        Personalização,
        on_delete=models.PROTECT,
        related_name='loja_Automotiva',
        verbose_name='Personalização',
    )

class Meta:
    verbose_name = 'loja_Automotiva',
    verbose_name_plural = 'loja_Automotivas'
    ordering = ['nome']

    def __str__(self):
        return self.nome

    
    def get_absolute_url(self):
        return reverse('loja_Automotiva', kwargs={'pk': self.pk})