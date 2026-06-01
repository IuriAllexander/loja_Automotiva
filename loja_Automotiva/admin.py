from django.contrib import admin
from .models import Categoria, Fabricante, Produto, Usuario, Pedido
# Register your models here.
 
admin.site.register(Categoria)
admin.site.register(Fabricante)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Pedido)