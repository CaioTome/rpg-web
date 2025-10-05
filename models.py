from config import db

class Personagem(db.Model):
    """
    Define a estrutura da tabela 'personagem' no banco de dados.
    Esta é a Camada de Acesso a Dados.
    """
    # Identificador único do personagem (chave primária)
    id = db.Column(db.Integer, primary_key=True)
    
    # Atributos definidos pelo usuário ou pelo jogo
    nome = db.Column(db.String(80), nullable=False)
    vida = db.Column(db.Integer, default=10)
    
    # Atributos customizados: ataque e defesa
    ataque = db.Column(db.Integer, default=5)
    defesa = db.Column(db.Integer, default=3)

    def __repr__(self):
        return f'<Personagem {self.nome} | Vida: {self.vida}>'
