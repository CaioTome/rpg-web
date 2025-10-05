from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria a instância do aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite:
# O arquivo do banco será criado na raiz do projeto.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rpg_db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão SQLAlchemy, mas não a associa diretamente ao app
# para evitar problemas de dependência circular.
db = SQLAlchemy(app)
