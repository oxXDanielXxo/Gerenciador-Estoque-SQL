# 📦 Sistema de Gerenciamento de Estoque (SQLite + Python)

Aplicativo desktop para controle de inventário local, com interface gráfica moderna em Dark Mode e integração direta com banco de dados relacional. Projetado para gerenciar componentes eletrônicos, peças mecânicas ou qualquer ativo físico que demande controle de entrada e leitura.

## 🚀 Arquitetura e Funcionalidades
* **Interface Gráfica (Frontend):** Construída com a biblioteca `customtkinter` para uma experiência de usuário (UX) fluida, substituindo o visual padrão do Windows por componentes estilizados.
* **Persistência de Dados (Backend):** Integração nativa com SQLite3. O sistema verifica a existência estrutural do banco na inicialização e executa o `CREATE TABLE` de forma autônoma.
* **Operações SQL (CRUD):** * Inserção (`INSERT`) de novos componentes validada e protegida contra SQL Injection (uso de queries parametrizadas).
  * Leitura (`SELECT`) de todo o inventário estruturada em uma janela flutuante dinamicamente dimensionada.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Banco de Dados:** SQLite3 (Embutido no Python, usando a mesma lógica de comandos do MySQL).
* **GUI (Interface):** CustomTkinter.

## ⚙️ Como Executar na Sua Máquina

### Instalação e Execução
1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/Gerenciador-Estoque-SQL.git](https://github.com/SEU-USUARIO/Gerenciador-Estoque-SQL.git)
   
2. Instale a biblioteca visual:
pip install customtkinter

3. Execute o motor principal:
python app.py