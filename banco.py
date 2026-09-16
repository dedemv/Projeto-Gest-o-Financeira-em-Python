import os
from arvore import ArvoreBinaria
from persistencia import salvar_tabela

ARQUIVOS_BANCOS = "bancos.txt"

class Banco:
    def __init__(self, cod_banco, descricao):
        self.cod_banco = int(cod_banco)
        self.descricao = descricao

    def to_linha(linha):
        cod, desc = linha.strip().split(";")
        return Banco(cod, desc)

    @staticmethod
    def from_linha(linha):
        cod, desc = linha.strip().split(";")
        return Banco(cod, desc)

arvore_banco = ArvoreBinaria()

def carregar_bancos():
    if os.path.exists(ARQUIVOS_BANCOS):
        with open(ARQUIVOS_BANCOS, "r", encoding="utf-8") as f:
            for linha in f:
                if linha.strip():
                    b = Banco.from_linha(linha)
                    arvore_banco.inserir(b.cod_banco, b)

def salvar_bancos():
    salvar_tabela(arvore_banco, ARQUIVOS_BANCOS, lambda b: b.to_linha())

def buscar_banco(codigo):
    no = arvore_banco.buscar(codigo)
    return no.valor if no else None

def cadastrar_banco ():
    print("\n Cadrastro do Banco: ")
    try:
        cod = int(input("Código do Banco: "))
    except ValueError:
        print("Erro: o código deve ser numérico!")
        return

    if buscar_banco(cod):
        print("Erro: Banco já cadastrado!")
        return

    desc = input("Nome/Descrição do Banco: ").strip()
    if not desc:
        print("ERRO: a descrição não pode ser vazia!")
        return

    banco = Banco(cod, desc)
    arvore_banco.inserir(cod, banco)
    salvar_bancos()
    print("Banco cadastrado com sucesso!")

def listar_bancos():
    bancos = arvore_banco.em_ordem()
    print("\n" + "=" * 40)
    print(f"{'Código':<8} _ {'Descrição':<28}")
    print("=" * 40)
    if not bancos:
        print("(Nenhum banco cadastrado)")
    for b in bancos:
        print(f"{b.cod_banco:<8} _ {b.descricao:<28}")
    print("=" * 48)