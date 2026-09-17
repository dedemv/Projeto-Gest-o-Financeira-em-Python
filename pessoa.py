import os
from arvore import ArvoreBinaria
from persistencia import salvar_tabela

ARQUIVOS_PESSOAS = "pessoas.txt"

class Pessoa:
    def __init__(self, codigo, nome):
        self.codigo = int(codigo)
        self.nome = nome

    def to_linha(self):
        return f"{self.codigo};{self.nome}"

    @staticmethod
    def from_linha(linha):
        cod, nome = linha.strip().split(";")
        return Pessoa(cod, nome)

arvore_pessoas = ArvoreBinaria()

def carregar_pessoas():
    if os.path.exists(ARQUIVOS_PESSOAS):
        with open(ARQUIVOS_PESSOAS, "r", encoding="utf-8") as f:
           for linha in f:
                if linha.strip():
                    p = Pessoa.from_linha(linha)
                    arvore_pessoas.inserir(p.codigo, p)

def salvar_pessoa():
    salvar_tabela(arvore_pessoas, ARQUIVOS_PESSOAS, lambda p: p.to_linha())

def buscar_pessoa(codigo):
    no = arvore_pessoas.buscar(codigo)
    return no.valor if no else None

def cadastrar_pessoa():
    print("\n --- Cadastro de Pessoa ---")
    try:
        cod = int(input("Código da Pessoa: "))
    except ValueError:
        print("Erro: o código deve ser numérico!")
        return
    if buscar_pessoa(cod):
        print("Erro: Código já cadastrado!")
        return
    nome = input("Nome da Pessoa: ").strip()
    if not nome:
        print("Erro: o nome não pode ser vazio!")
        return
    pessoa = Pessoa(cod, nome)
    arvore_pessoas.inserir(cod, pessoa)
    salvar_pessoa

def listar_pessoas():
    pessoas = arvore_pessoas.em_ordem()
    print("\n" + "=" * 40)
    print(f"{'Código':<8} _ {'Nome':<28}")
    print("=" * 40)
    if not pessoas:
        print("(Nenhuma pessoa cadastrada)")
    for p in pessoas:
        print(f"{p.codigo:<8} _ {p.nome:<28}")
    print("=" * 40)

    