import os
from arvore import ArvoreBinaria
from persistencia import salvar_tabela
from banco import buscar_banco
from pessoa import buscar_pessoa

ARQUIVO_CONTAS = "contas.txt"

class ContaBancaria:
    def __init__(self, cod_conta, cod_banco, cod_pessoa, descricao, saldo):
        self.cod_conta = int(cod_conta)
        self.cod_banco = int(cod_banco)
        self.cod_pessoa = int(cod_pessoa)
        self.descricao = descricao
        self.saldo = float(saldo)

    def to_linha(self): #caso o professor pergunte essa função é para colocar tudo as informações no txt
        return f"{self.cod_conta};{self.cod_banco};{self.cod_pessoa};{self.descricao};{self.saldo}"

    @staticmethod
    def from_linha(linha):
        cod_c, cod_b, cod_p, desc, saldo = linha.strip().split(";")
        return ContaBancaria(cod_c, cod_b, cod_p, desc, saldo)

arvore_contas = ArvoreBinaria()

def carregar_contas():
    if os.path.exists(ARQUIVO_CONTAS):
        with open(ARQUIVO_CONTAS, "r", encoding="utf-8") as f:
            for linha in f:
                if linha.strip():
                    c = ContaBancaria.from_linha(linha)
                    arvore_contas.inserir(c.cod_conta, c)

def salvar_contas():
    salvar_tabela(arvore_contas, ARQUIVO_CONTAS, lambda c: c.to_linha())

def buscar_contas(codigo):
    no = arvore_contas.buscar(codigo)
    return no.valor if no else None

def cadastrar_conta():
    print("\n --- Cadastro de Conta Bancaria ---")
    try:
        cod_c = int(input("Código da Conta: "))
    except ValueError:
        print("Erro: o código deve ser numérico!")
        return
    
    if buscar_contas(cod_c):
        print("Erro: Conta já cadastrada!")
        return

    try:
        cod_b = int(input("Código do Banco: "))
    except:
        print("Erro: o código do Banco deve ser numérico!")
        return

    banco = buscar_banco(cod_b)
    if not banco:
        print("Erro: Banco não encontrado!")
        return
    print(f"-> Banco Selecionado: {banco.descricao}")

    try:
        cod_p = int(input("Código da Pessoa: "))
    except:
        print("Erro: o código da Pessoa deve ser numérico!")
        return

    pessoa = buscar_pessoa(cod_p)
    if not pessoa:
        print("Erro: Pessoa não encontrada!")
        return
    print(f" --> Pessoa Selecionada: {pessoa.nome}")

    desc = input("Descrição da Conta (EX: Corrente, Poupança): ").strip()

    try:
        saldo = float(input("Saldo Inicial: R$ "))
    except ValueError:
        print("Erro: o saldo deve ser numérico!")
        return

    conta = ContaBancaria(cod_c, cod_b, cod_p, desc, saldo)
    arvore_contas.inserir(cod_c, conta)
    salvar_contas()
    print("Conta Bancária cadastrada com sucesso!")

def listar_contas():
    contas = arvore_contas.em_ordem()
    print(f"{'Cod':<5} _ {'Descrição':<18} _ {'Banco':<20} _ {'Titular':<20} _ {'Saldo':<10}")
    print("=" * 90)
    if not contas:
        print("(nenhuma conta cadastrada)")
    for c in contas:
        banco = buscar_banco(c.cod_banco)
        nome_banco = banco.descricao if banco else "N/A"
        pessoa = buscar_pessoa(c.cod_pessoa)
        nome_pessoa = pessoa.nome if pessoa else "N/A"
        print(f"{c.cod_conta:<5} _ {c.descricao:<18} _ {nome_banco:<20} _ {nome_pessoa:<20} _ R$ {c.saldo:<8.2f}")
    print("=" * 90)