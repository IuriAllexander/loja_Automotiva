from django.contrib import admin
from .models import Categoria, Fabricante, Personalização, loja_Automotiva
# Register your models here.
 
admin.site.register(Categoria)
admin.site.register(Fabricante)
admin.site.register(Personalização)
admin.site.register(loja_Automotiva)