from flask import render_template, request, redirect, url_for
from config import app, db
from services import PersonagemService # Importamos o Serviço para usar a lógica e o DAO
from models import Personagem # Importamos o Modelo apenas para o db.create_all()

# --- Rota Auxiliar: Criar o BD ---
with app.app_context():
    # Cria as tabelas no BD a partir dos modelos definidos em models.py
    # Execute isso toda vez que houver uma MUDANÇA na estrutura de 'models.py'
    db.create_all()

# --- Rota 1: Raiz (Ponto de Entrada) ---
@app.route('/')
def index():
    # Redireciona o usuário diretamente para a página de criação, um ponto de partida lógico
    return redirect(url_for('criar_personagem'))


# --- Rota 2: CRIAR (CREATE) ---
@app.route('/criar', methods=['GET', 'POST'])
def criar_personagem():
    if request.method == 'POST':
        # Coleta de dados na Camada de Apresentação
        nome = request.form.get('nome')
        try:
            # Captura os valores do formulário e converte para inteiro
            # Usando .get(key, default) para evitar erros se o campo não vier
            ataque = int(request.form.get('ataque', 5)) 
            defesa = int(request.form.get('defesa', 3))
        except ValueError:
            return "Erro: Ataque e Defesa devem ser números inteiros.", 400

        # APRESENTAÇÃO CHAMA SERVIÇO (Lógica de Negócio + DAO)
        try:
            PersonagemService.criar_novo_personagem(nome, ataque, defesa)
            return redirect(url_for('lista_personagens'))
        except Exception as e:
            print(f"Erro ao salvar o personagem: {e}")
            return "Erro interno ao salvar. Verifique o console.", 500
        
    # GET: Apenas exibe o formulário
    return render_template('criar_personagem.html')


# --- Rota 3: LER (READ) - Listar todos ---
@app.route('/lista')
def lista_personagens():
    # APRESENTAÇÃO CHAMA SERVIÇO (DAO)
    personagens = PersonagemService.listar_personagens()
    
    # Apresentação: Passa a lista para o template
    return render_template('lista_personagens.html', personagens=personagens)


# --- Rota 4: UPDATE (Lógica de Combate) ---
@app.route('/batalha/<int:personagem_id>')
def batalha(personagem_id):
    # APRESENTAÇÃO CHAMA SERVIÇO (Lógica de Combate)
    resultado = PersonagemService.combater_inimigo(personagem_id)

    if not resultado:
        return "Herói não encontrado.", 404
    
    # Recupera o herói atualizado para exibir na tela
    heroi_atualizado = PersonagemService.buscar_por_id(personagem_id)

    # Apresentação: Passa os dados de combate para o template
    return render_template('batalha.html', 
                           heroi=heroi_atualizado, 
                           log_combate=resultado.log, 
                           inimigo_vida=resultado.inimigo_vida)


if __name__ == '__main__':
    app.run(debug=True)
