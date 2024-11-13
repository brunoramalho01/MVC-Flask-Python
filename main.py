# Importa a instância da aplicação Flask criada em app/__init__.py
from app import app

# Executa a aplicação apenas se este arquivo for o ponto de entrada principal
if __name__ == "__main__":
    # Executa a aplicação Flask com modo de depuração ativado
    app.run(debug=True)
