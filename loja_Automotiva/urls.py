from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('categorias/', views.categorias_page, name='categorias'),


    path('login/', views.login_page, name='login'),
    path('cadastro/', views.cadastro_page, name='cadastro'),
    path('perfil/', views.perfil_page, name='perfil'),


    path('produto/', views.produto_page, name='produto'),


    path('adicionar/', views.adicionar_produto, name='adicionar'),

    path('carrinho/', views.carrinho_page, name='carrinho'),
    path('contato/', views.contato_page, name='contato'),

    path('chatbot/api/', views.responder_chatbot, name='responder_chatbot'),

    path('login-teste/', views.login_teste_page, name='login_teste'),

      path('cadastro-teste/', views.cadastro_teste_page, name='cadastro_teste'),

      path('servicos/', views.servicos_page, name='servicos'),

      path('pagamento_teste/', views.pagamento_teste_page, name='pagamento_teste'),
]
