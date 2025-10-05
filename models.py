from dataclasses import dataclass
# Importa o 'db' do nosso arquivo de configuração
from config import db

# Definição do Modelo (ORM - Object-Relational Mapper)
# Esta classe mapeia a tabela 'personagem' no banco de dados.

# Usamos @dataclass para fornecer métodos úteis de inicialização e representação.
@dataclass
class Personagem(db.Model):
    # Campos que serão lidos pelo HTML/JSON
    id: int
    nome: str
    vida: int
    forca: int
    
    # Colunas no Banco de Dados (ORM)
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    vida = db.Column(db.Integer, default=10)
    forca = db.Column(db.Integer, default=5)
    
    # Adicionamos um método que será a Lógica de Negócio central (preparando para a Etapa 4)
    def sofrer_dano(self, dano):
        """Reduz a vida do personagem."""
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
