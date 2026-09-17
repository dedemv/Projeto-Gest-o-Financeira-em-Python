import customtkinter as ctk
from pessoa import carregar_pessoas, cadastrar_pessoa, listar_pessoas
from categoria import carregar_categorias, cadastrar_categoria, listar_categoria
from banco import carregar_bancos, cadastrar_banco, listar_bancos
from conta import carregar_contas, cadastrar_conta, listar_contas
from transacao import carregar_transacoes, realizar_transacao, excluir_transacao
from relatorios import relatorio_transacoes_periodo, relatorio_saldos_contas

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Aplicativo(ctk.CTk): #esse parametro garante ser uma janela ao invez de ficar escrevendo em todos as linhas
    def __init__(self):
        super().__init__() #superclasse garante a execução dos parametros primeiro
        self.title("Sistema de Gestão Financeira")
        self.geometry("900x600")

        #divisao das telas
        self.grid_columnconfigure(1, weight=1) #expansão com a tela
        self.grid_rowconfigure(0, weight=1)

        #parte lateral
        self.barralateral = ctk.CTkFrame(self, width=200)
        self.barralateral.grid(row=0, column=0, sticky="nsew")
        #parte principal
        self.janelas_abas = ctk.CTkTabview(self, width=400)
        self.janelas_abas.grid(row=0, column=1, sticky="nsew", padx=10)

        self.construir_abalateral()

        self.construir_abaperfil()

        self.construir_preferencias()

        self.construir_abaSistema() 

    def construir_abalateral(self):
        self.titulo = ctk.CTkLabel(self.barralateral, text="Meu App", font=ctk.CTkFont(size=24, weight="bold"))
        self.titulo.pack(pady=(30, 10), padx=(20, 20))

        self.botao_principal = ctk.CTkButton(self.barralateral, text="Dashboard Principal")
        self.botao_principal.pack(pady=(30, 30), padx=(10, 10))

        self.switch_mododark = ctk.CTkSwitch(self.barralateral, text="Modo Escuro")
        self.switch_mododark.pack(pady=(10, 10), side="bottom") #command para funções do botao

    def construir_abaperfil(self):
        pass
    def construir_preferencias(self):
        pass
    def construir_abaSistema(self):
        pass







    
janela = Aplicativo()
janela.mainloop()


