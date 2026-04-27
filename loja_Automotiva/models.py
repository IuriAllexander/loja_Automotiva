from django.db import models

# Create your models here.

class Categoria (models.Model):
    pass 


class Fabricante(models.Model):
    pass


class Personalização(models.Model):
    rodas = models.CharField(max_length=150)
    escapamento = models.TextField(max_length=150)
    espelho = models.CharField(max_length=150)

    def __str__(self):
        return self.rodas


class loja_Automotiva(models.Model):
    pass