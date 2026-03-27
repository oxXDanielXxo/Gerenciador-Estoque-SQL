import sqlite3
import customtkinter as ctk


# ==========================================
# CAMADA DE BANCO DE DADOS (SQL)
# ==========================================
def inicializar_banco():
    conexao = sqlite3.connect('estoque.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS componentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            categoria TEXT
        )
    ''')
    conexao.commit()
    conexao.close()


def salvar_no_banco():
    nome = entry_nome.get()
    qtd = entry_qtd.get()
    cat = entry_cat.get()

    if nome == "" or qtd == "":
        lbl_status.configure(text="Erro: Nome e Quantidade são obrigatórios!", text_color="red")
        return

    try:
        conexao = sqlite3.connect('estoque.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO componentes (nome, quantidade, categoria) VALUES (?, ?, ?)", (nome, int(qtd), cat))
        conexao.commit()
        conexao.close()

        entry_nome.delete(0, 'end')
        entry_qtd.delete(0, 'end')
        entry_cat.delete(0, 'end')

        lbl_status.configure(text=f"[+] '{nome}' adicionado com sucesso!", text_color="green")

    except Exception as e:
        lbl_status.configure(text=f"Erro crítico no banco: {e}", text_color="red")


# O Pulo do Gato (O comando SELECT)
def buscar_estoque():
    try:
        conexao = sqlite3.connect('estoque.db')
        cursor = conexao.cursor()

        # Busca todas as linhas da tabela
        cursor.execute("SELECT * FROM componentes")
        linhas = cursor.fetchall()

        conexao.close()
        return linhas
    except Exception as e:
        print(f"Erro ao buscar: {e}")
        return []


# ==========================================
# CAMADA DE INTERFACE GRÁFICA (GUI)
# ==========================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Sistema de Estoque v1.2")
janela.geometry("500x500")  # Aumentei um pouco a altura


# --- Função da Nova Janela ---
def abrir_janela_estoque():
    # Cria uma janela secundária que fica por cima da principal
    janela_lista = ctk.CTkToplevel(janela)
    janela_lista.title("Estoque Atual")

    # AJUSTE 1: Aumentamos a janela para 750 pixels de largura por 450 de altura
    janela_lista.geometry("750x450")

    janela_lista.attributes("-topmost", True)

    ctk.CTkLabel(janela_lista, text="Itens Cadastrados", font=("Arial", 18, "bold")).pack(pady=10)

    # AJUSTE 2: Aumentamos a caixa de texto (width) para 700 para acompanhar a tela
    caixa_texto = ctk.CTkTextbox(janela_lista, width=700, height=350, font=("Consolas", 14))
    caixa_texto.pack(pady=10)

    # Executa a busca no banco
    itens = buscar_estoque()

    if len(itens) == 0:
        caixa_texto.insert("0.0", "O estoque está vazio.")
    else:
        # Preenche a caixa de texto linha por linha
        for item in itens:
            # A variável item é uma lista com: [id, nome, quantidade, categoria]
            texto_linha = f"ID: {item[0]} | Peça: {item[1]} | Qtd: {item[2]} | Cat: {item[3]}\n"
            caixa_texto.insert("end", texto_linha)

    # Trava a caixa para o usuário não conseguir apagar o texto digitando por cima
    caixa_texto.configure(state="disabled")


# --- Elementos Visuais ---
ctk.CTkLabel(janela, text="Novo Componente", font=("Arial", 20, "bold")).pack(pady=15)

entry_nome = ctk.CTkEntry(janela, placeholder_text="Nome da Peça", width=300)
entry_nome.pack(pady=10)

entry_qtd = ctk.CTkEntry(janela, placeholder_text="Quantidade", width=300)
entry_qtd.pack(pady=10)

entry_cat = ctk.CTkEntry(janela, placeholder_text="Categoria", width=300)
entry_cat.pack(pady=10)

btn_salvar = ctk.CTkButton(janela, text="Adicionar ao Estoque", command=salvar_no_banco, width=300, fg_color="#2E7D32",
                           hover_color="#1B5E20")
btn_salvar.pack(pady=15)

# O NOVO BOTÃO
btn_ver_estoque = ctk.CTkButton(janela, text="Ver Estoque Completo", command=abrir_janela_estoque, width=300)
btn_ver_estoque.pack(pady=5)

lbl_status = ctk.CTkLabel(janela, text="Pronto para registrar.", font=("Arial", 12))
lbl_status.pack(pady=5)

if __name__ == "__main__":
    inicializar_banco()
    janela.mainloop()