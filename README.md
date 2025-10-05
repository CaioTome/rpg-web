# **RPG de Texto \- Web Edition ⚔️**

Este é um projeto minimalista de um RPG de texto construído como ferramenta de aprendizado e portfólio. Ele demonstra a integração de um framework web (Flask), um banco de dados relacional (SQLite) e a aplicação de boas práticas de Engenharia de Software, como a **Arquitetura de 3 Camadas**.

## **🚀 Status do Projeto e Funcionalidades**

O projeto está em desenvolvimento ativo, focado em implementar o ciclo completo do CRUD (Create, Read, Update, Delete) com lógica de jogo real.

### **Funcionalidades Atuais (Etapas 1-3)**

* **Criação de Personagens (CREATE):** Formulário para nomear o herói com persistência inicial de atributos.  
* **Persistência de Dados (SQLite):** Utilização do Flask-SQLAlchemy (ORM) para salvar e carregar personagens permanentemente.  
* **Listagem de Heróis (READ):** Tela para visualizar todos os personagens criados e seus atributos.  
* **Estrutura Profissional:** Código organizado em arquitetura de 3 camadas.

### **Próximas Funcionalidades (Etapa 4 em diante)**

* **Combate (UPDATE):** Implementação da lógica de rolagem de dados e cálculo de dano, com atualização da vida no banco.  
* **Exclusão de Personagens (DELETE):** Rota para remover heróis.

## **📐 Arquitetura do Projeto (3 Camadas)**

O projeto segue o princípio de Separação de Preocupações, dividindo o código em camadas lógicas:

1. **Apresentação (`app.py` / `templates/`):** Lida com as rotas HTTP e a interface do usuário (HTML).  
2. **Lógica de Negócio (Implícito em `app.py` e `models.py`):** Define as regras do jogo e a manipulação dos dados (Ex: definição de atributos iniciais, futuros cálculos de ataque).  
3. **Acesso a Dados (`config.py` / `models.py`):** Responsável pela conexão e mapeamento do banco de dados (SQLite via Flask-SQLAlchemy).

**Estrutura de Arquivos:**

/seu\_projeto  
├── app.py              \# Camada de Apresentação (Rotas)  
├── config.py           \# Configuração da Aplicação e Banco (Inicialização)  
├── models.py           \# Camada de Acesso a Dados (Modelo Personagem / ORM)  
├── templates/          \# Apresentação (Templates HTML)  
├── static/             \# Apresentação (Estilos CSS)  
└── rpg\_db.sqlite       \# Banco de Dados (Gerado automaticamente)

## **🛠️ Instalação e Execução**

### **Pré-requisitos**

* Python 3.13

### **1\. Clonar o Repositório (ou criar os arquivos)**

\# Se estiver usando Git  
git clone \<URL\_DO\_SEU\_REPO\>  
cd \<nome\_do\_seu\_repo\>

### **2\. Configurar o Ambiente Virtual**

É obrigatório o uso de um ambiente virtual (venv) para isolar as dependências.

python \-m venv venv

### **3\. Ativar o Ambiente e Instalar Dependências**

Certifique-se de que o seu `venv` está ativo.

| Sistema Operacional | Comando de Ativação |
| ----- | ----- |
| Windows (CMD) | `venv\Scripts\activate.bat` |
| macOS/Linux | `source venv/bin/activate` |

Instale os pacotes necessários:

pip install Flask

pip install flask_sqlalchemy

### **4\. Executar a Aplicação**

O Flask irá criar o arquivo `rpg_db.sqlite` automaticamente na primeira execução.

python app.py

Acesse a aplicação no seu navegador: **`http://127.0.0.1:5000/`**
