# **⚔️ RPG de Texto: Web Edition ⚔️**

Aplicação web minimalista de RPG de texto construída em Python com o framework Flask e persistência de dados utilizando SQLite. O foco principal deste projeto é demonstrar a aplicação de **boas práticas de Engenharia de Software**, arquitetura limpa e o padrão CRUD (Create, Read, Update, Delete).

## **💡 Escolhas de Tecnologias**

| Tecnologia | Finalidade | Justificativa de Escolha |
| ----- | ----- | ----- |
| **Python 3** | Linguagem de Back-end. | Simplicidade, facilidade de prototipagem e vasto ecossistema. |
| **Flask** | Micro-Framework Web. | Leveza e minimalismo. Escolhido para focar na arquitetura pura da aplicação em vez de abstrações complexas. |
| **SQLite** | Banco de Dados. | Utilizado para persistência local dos dados, ideal para ambientes de desenvolvimento. |
| **Flask-SQLAlchemy** | ORM (Mapeador Objeto-Relacional). | Abstrai a manipulação de dados em Python. |
| **Bootstrap 5** | Front-end/CSS. | Usado para garantir uma interface visual rápida e responsiva. |

## **🏗️ Arquitetura, Padrões e Decisões de Engenharia de Software**

O projeto é estruturado seguindo o princípio de **Separação de Preocupações**, utilizando uma Arquitetura de 3 Camadas e aplicando Padrões de Projeto específicos.

### **Padrões de Projeto Utilizados**

#### **1\. DAO (Data Access Object) / Service Layer**

* **Onde é Aplicado:** No arquivo `services.py`.  
* **Decisão:** O DAO isola a lógica de acesso ao banco de dados (o `db.session` e o ORM). A **Camada de Serviço** encapsula esse DAO, adicionando a **Lógica de Negócio** (ex: o cálculo de dano na função `combater_inimigo`).  
* **Benefício:** Se o banco de dados mudar (ex: de SQLite para PostgreSQL), ou se o ORM mudar, apenas o `services.py` e `models.py` precisam ser ajustados, deixando as rotas (`app.py`) inalteradas.

#### **2\. Model-View-Controller (MVC)**

* **Onde é Aplicado:** Na divisão geral do projeto.  
* **Adaptação Flask:**  
  * **Model:** O `models.py` (estrutura dos dados).  
  * **View:** Os arquivos HTML em `templates/` (o que o usuário vê).  
  * **Controller:** O `app.py` e, em parte, o `services.py` (onde a requisição é recebida e a lógica de ação é disparada).

### **Estrutura em Camadas**

| Camada | Arquivos | Responsabilidade |
| ----- | ----- | ----- |
| **Apresentação (Controller/View)** | `app.py`, `templates/` | Recebe a requisição, coleta dados do formulário (`request.form`) e exibe o resultado. Não contém lógica de persistência. |
| **Serviço (Lógica de Negócio)** | `services.py` | Regras do jogo (rolagem de dado, cálculo de dano) e orquestração do acesso a dados via DAO. |
| **Acesso a Dados (Model)** | `models.py`, `config.py` | Mapeamento da classe `Personagem` para a tabela do SQLite (ORM). |

## **⚙️ Como Executar o Projeto**

Siga estes passos no seu terminal (com o `venv` ativado):

1. **Ative o Ambiente Virtual (`venv`):**  
   * Windows (CMD): `venv\Scripts\activate.bat`  
   * Linux/macOS (Bash): `source venv/bin/activate`

**Rode o Servidor:**  
python app.py

2.   
3. **Acesse:** Abra seu navegador e acesse `http://127.0.0.1:5000/`.

**NOTA:** Se você alterou a estrutura do banco (`models.py`), certifique-se de **deletar o arquivo `rpg_db.sqlite`** antes de rodar o `python app.py` novamente.
