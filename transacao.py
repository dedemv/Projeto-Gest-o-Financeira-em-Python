import os
from arvore import ArvoreBinaria
from persistencia import salvar_tabela
from categoria import buscar_categoria
from conta import buscar_contas, salvar_contas
from banco import buscar_banco

ARQUIVO_TRANSACOES = "transacoes.txt"

class Transacao:
    def __init__(self, codigo_trans, cod_cat, cod_conta, data, valor, debito_credito):
        self.codigo_trans = int(codigo_trans)
        self.cod_cat = int(cod_cat)
        self.cod_conta = int(cod_conta)
        self.data = data
        self.valor = float(valor)
        self.debito_credito = debito_credito

    def to_linha(self):
        return f"{self.codigo_trans};{self.cod_cat};{self.cod_conta};{self.data};{self.valor};{self.debito_credito}"

    @staticmethod
    def from_linha(linha):
        cod_t, cod_cat, cod_conta, data, valor, op = linha.strip().split(";")
        return Transacao(cod_t, cod_cat, cod_conta, data, valor, op)

arvore_transacoes = ArvoreBinaria()

def carregar_transacoes():
    if os.path.exists(ARQUIVO_TRANSACOES):
        with open(ARQUIVO_TRANSACOES, "r", encoding="utf-8") as f:
            for linha in f:
                if linha.strip():
                    t = Transacao.from_linha(linha)
                    arvore_transacoes.inserir(t.codigo_trans, t)

def salvar_transacoes():
    salvar_tabela(arvore_transacoes, ARQUIVO_TRANSACOES, lambda t: t.to_linha())

def buscar_transacao(codigo):
    no = arvore_transacoes.buscar(codigo)
    return no.valor if no else None

def realizar_transacao():
    print("\n --- Lançamento de Transação Financeira ---")
    try:
        cod_t = int(input("Código da Transação: "))
    except:
        print("Erro: o código deve ser numérico!")
        return

    if buscar_transacao(cod_t):
        print("Erro: Transação já existe!")
        return

    try:
        cod_cat = int(input("Código da Categoria: "))
    except ValueError:
        print("Erro: o cóidigo da Categoria deve ser numérico!")
        return

    categoria =  buscar_categoria(cod_cat)
    if not categoria:
        print("Erro: Categoria não encontrada!")
        return
    print(f"--> Categoria: {categoria.descriacao}")

    try:
        cod_conta = int(input("Código da Conta Bancária: "))
    except ValueError:
        print("Erro: Conta Bancária não encontrada!")
        return

    conta = buscar_contas(cod_conta)
    if not conta:
        print("Erro: Conta Bancária não encontrada!")
        return

    banco = buscar_banco(conta.cod_banco)
    nome_banco = banco .descricao if banco else "Desconhecido"
    print(f"--> Banco da Conta: {nome_banco}")

    data = input("Data (AAAA-MM-DD): ").strip()

    try:
        valor = float(input("Valor da Transação: R$ "))
    except ValueError:
        print("Erro: o valor deve ser numérico!")
        return

    op = input("Operação - (C)rédito ou (D)ébito: ").strip().upper()
    if op not in ("C", "D"):
        print("Erro: Operação Inválida! Use apenas 'C' ou 'D'.")
        return

    if op == "C":
        conta.saldo += valor
    else:
        conta.valor += valor

    trasacao = Transacao(cod_t, cod_cat, cod_conta, data, valor, op)
    arvore_transacoes.inserir(cod_t, trasacao)

    salvar_transacoes()
    salvar_contas()
    print(f"Transação realizada! Novo Slado da Conta {cod_conta}: R$ {conta.saldo:2f}")

def excluir_transacao():
    print("\n --- Exclusão de Transação ---")
    try:
        cod_t = int(input("Digite o Código da Transação que deseja excluir: "))
    except ValueError:
        print("Erro: o código deve ser númerico!")
        return

    transacao = buscar_transacao(cod_t)
    if not transacao:
        print("Erro: Transação não encontrada!")
        return

    conta = buscar_contas(transacao.cod_conta)
    if conta:
        if transacao.debito_credito == "C":
            conta.saldo -= transacao.valor
        else:
            conta.saldo += transacao.valor

    arvore_transacoes.remover(cod_t)

    salvar_transacoes()
    salvar_contas()
    print(f"Transação {cod_t} excluida com sucesso e saldo da conta estornado!")
