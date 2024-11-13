# ModeloProjetos - Aplicação Flask

Este projeto é uma estrutura básica para desenvolver aplicações web usando o framework Flask. A organização segue o padrão MVC (Model-View-Controller), facilitando o desenvolvimento, organização e manutenção do código.

## Estrutura de Diretórios

        Aplicattion
        │   main.py
        │   
        └───app
            │   forms.py
            │   models.py
            │   routes.py
            │   __init__.py
            │   
            ├───static
            └───templates


## Descrição dos Arquivos e Pastas
- **main.py:** Arquivo principal que executa a aplicação Flask. Ele importa a instância da aplicação e a executa em modo de depuração.
- **app/__init__.py:** Inicializa a aplicação Flask, configura o ambiente e importa as rotas definidas em `routes.py`.
- **app/forms.py:** Define os formulários da aplicação. Esse arquivo pode usar a biblioteca Flask-WTF para validar e tratar entradas de usuário.
- **app/models.py:** Define os modelos e estruturas de dados do banco, com SQLAlchemy (ou outra biblioteca ORM), possibilitando a criação e manipulação das tabelas de dados.
- **app/routes.py:** Define as rotas (URLs) e as funções de visualização associadas. As rotas controlam o que é exibido ao usuário ao acessar URLs específicas.
- **app/static:** Contém arquivos estáticos como CSS, JavaScript e imagens.
- **app/templates:** Contém os arquivos HTML que compõem as páginas da aplicação.


## Funcionamento dos Arquivos

- **main.py:** Executa a aplicação, importando a instância Flask criada em `app/__init__.py` e definindo o modo de depuração.
- **app/__init__.py:** Inicializa a aplicação e importa as rotas. Este é o ponto onde a aplicação Flask é configurada.
- **app/forms.py:** Define os formulários que são usados em rotas específicas para coletar e validar entradas dos usuários.
- **app/models.py:** Define as classes de modelos do banco de dados, representando as tabelas e possibilitando o mapeamento objeto-relacional.
- **app/routes.py:** Define as rotas, mapeando URLs para funções de visualização que geram a resposta HTML ou JSON.

## Como Executar o Projeto
1. Clone o repositório.
2. Instale as dependências (caso esteja usando um ambiente virtual):
    ```bash
    pip install -r requirements.txt
3. Inicie a aplicação com o comando:
    ```bash
    python main.py
4. Acesse http://127.0.0.1:5000 em seu navegador para ver a aplicação em execução.

# Exemplo de Código nos Arquivos
## main.py

    from app import app

    if __name__ == "__main__":
        app.run(debug=True)

## app/__init__.py

    from flask import Flask

    app = Flask(__name__)

    from  app import routes

## app/forms.py

    # Aqui é onde serão tratados os formulários da aplicação
    # Exemplo de importação de FlaskForm
    # from flask_wtf import FlaskForm
    # from wtforms import StringField, SubmitField
    # from wtforms.validators import DataRequired

    # class ExampleForm(FlaskForm):
    #     name = StringField('Name', validators=[DataRequired()])
    #     submit = SubmitField('Submit')

## app/models.py

    # Aqui é onde será criada a estrutura do banco de dados da aplicação
    # from flask_sqlalchemy import SQLAlchemy

    # db = SQLAlchemy()

    # class User(db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    #     username = db.Column(db.String(80), unique=True, nullable=False)
    #     email = db.Column(db.String(120), unique=True, nullable=False)

    #     def __repr__(self):
    #         return f'<User {self.username}>'

## app/routes.py

    from flask import render_template, url_for
    from app import app

    @app.route('/')
    def home():
        return ('Hello World!')