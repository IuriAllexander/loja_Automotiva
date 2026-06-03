from django.contrib import admin
from .models import Categoria, Fabricante, Personalizacao, Loja_Automotiva
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao','codigo')
    search_fields = ('nome',)


@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nome','pais_origem','ano_fundacao',)
    search_fields = ('nome',)


@admin.register(Personalizacao)
class PersonalizacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo','tamanho','marca',)
    search_fields = ('tipo',)
    list_filter = ('marca',)


@admin.register(Loja_Automotiva)
class Loja_AutomotivaAdmin(admin.ModelAdmin):
    list_display = ('nome','endereco','telefone',)
    list_filter = ('nome',)
    search_fields = ('nome',)



