import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.font import Font
from pessoa import carregar_pessoas, cadastrar_pessoa, listar_pessoas
from categoria import carregar_categorias, cadastrar_categoria, listar_categoria
from banco import carregar_bancos, cadastrar_banco, listar_bancos
from conta import carregar_contas, cadastrar_conta, listar_contas
from transacao import carregar_transacoes, realizar_transacao, excluir_transacao
from relatorios import relatorio_transacoes_periodo, relatorio_saldos_contas


janela = tk.Tk()
janela.title("Sistema de Gestão Financeira")
janela.geometry("900x600")

titulo = tk.Label(text="Menu do meu APP", font=Font(size=22, weight="bold", family="Arial"))
titulo.pack(pady=(20, 20))
titulo = tk.Label(text="BEM VINDO!!")
titulo.pack(pady=(20, 20))

janela.mainloop()