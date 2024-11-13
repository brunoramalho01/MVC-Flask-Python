# Aqui é onde serão criadas as rotas para a aplicação funcionar

# Importa funções e variáveis do Flask necessárias para as rotas
from flask import render_template, url_for
# Importa a instância da aplicação Flask para que as rotas possam ser registradas
from app import app

# Define a rota para a página inicial da aplicação
@app.route('/')
def home():
    # Retorna uma resposta simples "Hello World!" como exemplo
    return ('Hello World!')
