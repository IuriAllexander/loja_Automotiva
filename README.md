# Marquinhos Autopeças

## Descrição

A **Marquinhos Autopeças** é uma aplicação web desenvolvida com Django para comercialização de peças automotivas. O sistema permite que usuários realizem cadastro, autenticação, naveguem pelos produtos disponíveis, filtrem itens por categorias, adicionem produtos ao carrinho e simulem o processo de compra.

O projeto foi desenvolvido utilizando o padrão MVC/MVT do Django, aplicando conceitos de modelagem de banco de dados, gerenciamento de usuários, organização de templates e persistência de dados. A aplicação busca oferecer uma experiência simples e intuitiva para clientes interessados na aquisição de peças automotivas.

# Equipe

| Integrante | GitHub          |
| ---------- | --------------- |
| IURI ALLEXANDER DE MELO TORRES BARRETO   | @IuriAllexandder |
| ISABELE EDUARDA BARBOSA MACÊDO           | @isabele-eduarda |
| DANILO JOSE DA SILVA                     | @DanNiloExe |

## Backend

* Python 3.x
* Django 6.0.4

## Banco de Dados

* SQLite3 (desenvolvimento)
* PostgreSQL (produção)

## Bibliotecas

* Pillow 12.2.0
* asgiref 3.11.1
* sqlparse 0.5.5
* tzdata 2026.2

## Frontend

* HTML5
* CSS3
* JavaScript

---

# Funcionalidades Implementadas

### Escopo Base

* Cadastro de usuários
* Login de usuários
* Gerenciamento de perfil
* Visualização de produtos
* Pesquisa de produtos por categorias
* Carrinho de compras
* Cadastro de pedidos
* Cadastro de fabricantes
* Cadastro de categorias
* Upload de imagens dos produtos
* Controle de estoque
* Chatbot simples para auxílio

---

# Modelagem do Sistema

O sistema possui as seguintes entidades principais:

## Categoria

Responsável pela classificação dos produtos em diferentes categorias automotivas.

### Atributos

* código da categoria
* nome da categoria
* descrição

---

## Fabricante

Armazena informações sobre os fabricantes das peças.

### Atributos

* nome
* CNPJ
* endereço
* telefone
* e-mail
* website
* país de origem

---

## Usuário

Representa os clientes cadastrados na plataforma.

### Atributos

* nome
* CPF
* e-mail
* telefone
* endereço

---

## Produto

Representa as peças automotivas comercializadas.

### Atributos

* código do produto
* nome
* preço
* estoque
* peso
* descrição
* imagem

### Relacionamentos

* pertence a uma categoria
* pertence a um fabricante

---

## Pedido

Representa as compras realizadas pelos usuários.

### Atributos

* identificador
* valor total
* data do pedido
* quantidade
* forma de pagamento

### Relacionamentos

* pertence a um usuário
* possui um ou mais produtos

---

# Pré-requisitos

Antes de executar o projeto, certifique-se de possuir instalado:
* Python 3.10 ou superior
* pip
* Git
* virtualenv (recomendado)

---

# Como Executar o Projeto

## 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/loja_automotiva.git
cd loja_automotiva
```

## 2. Criar e Ativar Ambiente Virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

## 4. Aplicar Migrações
```bash
python manage.py migrate
```

## 5. Criar Superusuário (Opcional)
```bash
python manage.py createsuperuser
```

## 6. Executar o Servidor
```bash
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000/
```

---

# Usuários de Teste

## Administrador

Usuário:

```text
admin
```

Senha:

```text
admin123
```

---

## Cliente

Usuário:

```text
cliente
```

Senha:

```text
cliente123
```

---

# Estrutura do Projeto

```text
loja_Automotiva/
│
├── core/
├── loja_Automotiva/
│   ├── migrations/
│   ├── templates/
│   │   ├── components/
│   │   ├── home/
│   │   ├── pages/
│   │   ├── partials/
│   │   └── base.html
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── usuarios/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# Screenshots

Adicionar imagens das principais telas na pasta `/docs`:

* Página Inicial
* Login
* Cadastro
* Catálogo de Produtos
* Carrinho de Compras
* Perfil do Usuário

Exemplo:

```text
docs/home.png
docs/cadastro.png
docs/login.png
docs/carrinho.png
docs/perfil.png
docs/pagamento.png
```

---

# Diagrama Entidade-Relacionamento


```text
docs/DER.png
```

Relacionamentos principais:

* Categoria 1:N Produto
* Fabricante 1:N Produto
* Usuário 1:N Pedido
* Pedido N:N Produto

---

# Licença

Projeto desenvolvido para fins acadêmicos como prática de desenvolvimento web utilizando Django.
