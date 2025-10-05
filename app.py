from flask import render_template, request, redirect, url_for
from config import app, db
from models import Personagem

# --- Rota Auxiliar: Criar o BD ---
# Você precisa rodar esta função APENAS UMA VEZ para criar o arquivo .sqlite
with app.app_context():
    # Cria as tabelas no BD a partir dos modelos definidos em models.py
    db.create_all()

# --- Rota 1: Raiz ---
@app.route('/')
def index():
    # MELHORIA DE UX: Redireciona o usuário diretamente para a página de criação de personagem.
    # Isso elimina o placeholder e guia o usuário para a ação principal.
    return redirect(url_for('criar_personagem'))


# --- Rota 2: CRIAR (CREATE) ---
@app.route('/criar', methods=['GET', 'POST'])
def criar_personagem():
    if request.method == 'POST':
        nome = request.form.get('nome')
        
        # 1. Lógica de Negócio: Definição de atributos iniciais
        novo_personagem = Personagem(nome=nome)
        
        # 2. Acesso a Dados: Salva no BD
        try:
            db.session.add(novo_personagem)
            db.session.commit()
            return redirect(url_for('lista_personagens'))
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao criar personagem: {e}")
            return "Erro ao salvar o personagem.", 500
        
    # GET: Apenas exibe o formulário (Cuidado: certifique-se de ter o arquivo criar_personagem.html!)
    return render_template('criar_personagem.html')


# --- Rota 3: LER (READ) ---
@app.route('/lista')
def lista_personagens():
    # Acesso a Dados: Consulta o BD para buscar TODOS
    personagens = Personagem.query.all()
    
    # Apresentação: Passa a lista para o template
    return render_template('lista_personagens.html', personagens=personagens)


if __name__ == '__main__':
    # Rodar o app agora usará a instância 'app' importada de config.py
    app.run(debug=True)
