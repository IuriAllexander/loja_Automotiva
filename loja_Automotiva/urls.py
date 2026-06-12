from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/', views.paginaCategoria, name='categoria'),


    path('login/', views.login_page, name='login'),
    path('cadastro/', views.cadastro_page, name='cadastro'),
    path('perfil/', views.perfil_page, name='perfil'),


    path('categoria/', views.paginaCategoria, name='categoria'),
    path('categorias/', views.categorias_page, name='categorias'),
    path('produtos/', views.produtos_page, name='produtos'),


    path('carrinho/', views.carrinho_page, name='carrinho'),
    path('contato/', views.contato_page, name='contato'),

    path('chatbot/api/', views.responder_chatbot, name='responder_chatbot'),
]