from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Define o caminho absoluto para o banco de dados SQLite
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'rpg_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy (o ORM)
db = SQLAlchemy(app)
