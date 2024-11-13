# Importa o módulo Flask para criar a aplicação
from flask import Flask

# Cria a instância principal da aplicação Flask
app = Flask(__name__)

# Importa as rotas da aplicação para que estejam disponíveis
from app import routes
