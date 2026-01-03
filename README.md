## Requistos

* Python 3 ou superior - Conferir a versão: python --version
* Django 5 ou superior - Conferir a versão: django-admin --version
* GIT - Conferir a instalação: git -v
* MySQL 8 ou superior - Conferir a versão: mysql --version

## Como rodar o projeto baixado

Instalar o Django.
```
pip install Django
```

Instalar o django-tinymce.
```
pip install django-tinymce
```

Instalar o conector MySQL.
```
pip install mysqlclient
```

Alterar no arquivo "settings.py" as credenciais do banco de dados<br>

Executa as migration.
```
python manage.py migrate
```

Rodar o projeto.
```
python manage.py runserver
```

Acessar o padrão do Python.
```
http://127.0.0.1:8000/
```

Criar um super usuário.
```
python manage.py createsuperuser
```
```
Usuário (leave blank to use 'cesar'): admin
Endereço de email: cesar@celke.com.br
Password: 123456A#
Password (again): 123456A#
```

Acessar o sistema administrativo padrão do Python.
```
http://127.0.0.1:8000/admin
```

Executar as seeds para cadastrar registro de teste.
```
python manage.py seed_courses
python manage.py seed_about
```

## Sequencia para criar o projeto

Instalar o Django.
```
pip install Django
```

Desinstalar o Django.
```
pip uninstall Django
```

Criar o projeto com Django.
```
django-admin startproject admin .
```

Rodar o projeto.
```
python manage.py runserver
```

Acessar o padrão do Python.
```
http://127.0.0.1:8000/
```

meu_projeto/<br>
│<br>
├── manage.py              # Ferramenta CLI para gerenciar o projeto<br>
├── meu_projeto/           # Diretório principal do projeto<br>
│   ├── __init__.py        # Identifica o diretório como um módulo Python<br>
│   ├── settings.py        # Configurações do projeto<br>
│   ├── urls.py            # Rotas principais do projeto<br>
│   ├── asgi.py            # Configuração para ASGI<br>
│   └── wsgi.py            # Configuração para WSGI<br>

Executa as migration.
```
python manage.py migrate
```

Instalar o conector MySQL.
```
pip install mysqlclient
```

Criar a base de dados.
```
CREATE DATABASE celke CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Executar as migrations para criar as tabelas.
```
python manage.py migrate
```

Criar um super usuário.
```
python manage.py createsuperuser
```

Acessar o sistema administrativo padrão do Python.
```
http://127.0.0.1:8000/admin
```

Criar novo app.
```
python manage.py startapp nome-do-app
```
```
python manage.py startapp courses
```

Criar migrations.
```
python manage.py makemigrations --name nome-da-migration
```
```
python manage.py makemigrations --name create_courses
```

Instalar o django-tinymce.
```
pip install django-tinymce
```

Instalar o Bootstrap.
```
pip install django-bootstrap-v5
```

## Como usar o GitHub

Baixar os arquivos do GitHub.
```
git clone -b <branch_nome> <repositorio_url> .
```

Verificar a branch.
```
git branch
```

Baixar as atualizações.
```
git pull
```

Adicionar todos os arquivos modificados para staging area - área de preparação.
```
git add .
```

commit representa um conjunto de alterações em um ponto específico da história do seu projeto, registra apenas as alterações adicionadas ao índice de preparação.
O comando -m permite que insira a mensagem de commit diretamente na linha de comando.
```
git commit -m "Descrição do commit"
```

Enviar os commits locais, para um repositório remoto.
```
git push <remote> <branch>
git push origin develop
```

Remover o arquivo do cache do GIT.
```
git rm --cached db.sqlite3
```

Remover o diretório do cache do GIT.
```
git rm --cached -r admin/__pycache__/
```