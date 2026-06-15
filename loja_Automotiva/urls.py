from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('produto/<int:pk>', views.produto_page, name='produto-detalhe'),
    path('categorias/', views.categorias_page, name='categorias'),
    path('categorias/<int:pk>', views.categoria_especifica, name='categoria-especifica'),

    path('perfil/', views.perfil_page, name='perfil'),


    path('criar/produto', views.criar_produto, name='criar-produto'),
    path('criar/categoria', views.criar_categoria, name='criar-categoria'),
    path('criar/fabricante', views.criar_fabricante, name='criar-fabricante'),

    path('produto/<int:pk>/editar/', views.editar_produto, name='editar-produto'),
    path('produto/<int:pk>/excluir/', views.excluir_produto, name='excluir-produto'),


    path('carrinho/', views.carrinho_page, name='carrinho'),
    path('contato/', views.contato_page, name='contato'),

    path('chatbot/api/', views.responder_chatbot, name='responder_chatbot'),

    path('servicos/', views.servicos_page, name='servicos'),

    path('pagamento_teste/', views.pagamento_teste_page, name='pagamento_teste'),
]
