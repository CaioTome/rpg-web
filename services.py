import random
from config import db
from models import Personagem
from collections import namedtuple

# Objeto simples para armazenar o resultado do combate
ResultadoCombate = namedtuple("ResultadoCombate", ["personagem_vida", "inimigo_vida", "log"])

def rolar_dado(lados=6):
    """Lógica de negócio simples: rolar um dado."""
    return random.randint(1, lados)

# --- DAO (Data Access Object) para Personagem e Lógica de Combate ---
class PersonagemService:
    @staticmethod
    def criar_novo_personagem(nome, ataque_base, defesa_base):
        """
        Lógica de Negócio: Cria uma nova instância de Personagem com atributos customizados.
        """
        novo_personagem = Personagem(
            nome=nome,
            vida=10,
            ataque=ataque_base,
            defesa=defesa_base
        )
        
        # Acesso a Dados (DAO: Persistência)
        db.session.add(novo_personagem)
        db.session.commit()
        return novo_personagem

    @staticmethod
    def listar_personagens():
        """Acesso a Dados: Busca todos os personagens no BD."""
        return Personagem.query.all()
    
    @staticmethod
    def buscar_por_id(id):
        """Acesso a Dados: Busca um personagem específico."""
        return Personagem.query.get(id)
    
    @staticmethod
    def combater_inimigo(personagem_id):
        """
        Lógica de Combate (UPDATE no BD).
        Simula um ataque contra um inimigo e atualiza a vida do herói.
        """
        heroi = PersonagemService.buscar_por_id(personagem_id)
        
        if not heroi:
            return None, "Herói não encontrado."

        # Inimigo (Hardcoded, para simplicidade)
        inimigo_vida_inicial = 6
        inimigo = {'nome': 'Goblin Furioso', 'ataque': 4, 'defesa': 1, 'vida': inimigo_vida_inicial}
        
        log_combate = []
        dado_heroi = rolar_dado()
        
        # 1. Ataque do Herói
        dano_bruto_heroi = heroi.ataque + dado_heroi
        dano_real_heroi = max(0, dano_bruto_heroi - inimigo['defesa'])
        
        inimigo['vida'] -= dano_real_heroi
        log_combate.append(f"{heroi.nome} atacou! Dado: {dado_heroi}. Dano causado ao {inimigo['nome']}: {dano_real_heroi}.")
        
        if inimigo['vida'] <= 0:
            log_combate.append(f"O {inimigo['nome']} foi derrotado! Herói Venceu!")
            db.session.commit() # Salva a vida atualizada do herói (se houver cura no futuro)
            return ResultadoCombate(heroi.vida, 0, log_combate)
        
        # 2. Contra-Ataque do Inimigo
        dado_inimigo = rolar_dado()
        dano_bruto_inimigo = inimigo['ataque'] + dado_inimigo
        dano_real_inimigo = max(0, dano_bruto_inimigo - heroi.defesa)
        
        heroi.vida -= dano_real_inimigo
        log_combate.append(f"{inimigo['nome']} contra-atacou! Dado: {dado_inimigo}. Dano recebido pelo {heroi.nome}: {dano_real_inimigo}.")

        # 3. Verificação de Morte do Herói
        if heroi.vida <= 0:
            heroi.vida = 0 # Não deixa vida negativa
            log_combate.append(f"Seu herói {heroi.nome} foi nocauteado! Fim de Jogo.")
            # Poderíamos adicionar lógica de deletar ou resetar o herói aqui.

        # 4. Acesso a Dados (DAO: Salva o novo estado de vida no BD)
        try:
            db.session.add(heroi)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            log_combate.append(f"Erro no BD: {e}")
            
        return ResultadoCombate(heroi.vida, inimigo['vida'], log_combate)

    # Futuramente, teremos aqui métodos como 'deletar_personagem'
