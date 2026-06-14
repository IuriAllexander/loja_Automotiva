# 🏁 Marquinhos Autopeças - Sistema de Gerenciamento e E-commerce

O **Marquinhos Autopeças** é uma aplicação web desenvolvida em Django para o gerenciamento de inventário e venda de peças automotivas de alta performance. O sistema permite o cadastro de produtos, categorização inteligente, controle de estoque e uma interface fluida para o cliente final.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.14+ e Django Framework
* **Banco de Dados:** SQLite (Ambiente de Desenvolvimento)
* **Frontend:** HTML5, CSS3 (Arquitetura responsiva com +900 linhas de estilização dedicada)
* **Controle de Versão:** Git & GitHub

---

## 🏗️ Arquitetura e Estrutura do Projeto

O projeto segue o padrão MVT (Model-View-Template) do Django. Recentemente, a estrutura passou por uma refatoração crítica de infraestrutura para garantir a integridade dos dados:

```text
loja_Automotiva/
│
├── manage.py                # Arquivo de gerenciamento do Django
├── .gitignore               # Blindagem de arquivos locais (venv, DB, cache)
│
├── static/                  # Arquivos estáticos globais
│   └── css/
│       └── style.css        # Estilização completa do ecossistema (+911 linhas)
│
├── loja_Automotiva/         # Core do projeto (Settings, URLs)
│   ├── settings.py          # Configurações absolutas de STATIC e MEDIA
│   └── ...
│
└── core_app/                # Aplicativo principal do e-commerce (ou nome do seu app)
    ├── models.py            # Modelagem corrigida (Produto, Categoria)
    ├── migrations/          # Histórico de migrações limpo e sincronizado
    └── templates/           # Arquivos HTML (index, partials)


1. Criar e Ativar o Ambiente Virtual

# No Windows:
python -m venv venv
.\venv\Scripts\activate


2. Instalar as Dependências

pip install django


3. Aplicar as Migrações

python manage.py makemigrations
python manage.py migrate


4.Criar um Usuário Administrador

python manage.py createsuperuser


5. Iniciar o Servidor

python manage.py runserver


