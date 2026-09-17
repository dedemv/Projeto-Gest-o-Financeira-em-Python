import os
from arvore import ArvoreBinaria
from persistencia import salvar_tabela

ARQUIVOS_CATEGORIA = "categoria.txt"

class Categoria:
    def __init__(self, codigo_cat, descricao):
        self.codigo_cat = int(codigo_cat)
        self.descricao = descricao

    def to_linha(self):
        return f"{self.codigo_cat};{self.descricao}"

    @staticmethod
    def from_linha(linha):
        cod, desc = linha.strip().split(";")
        return Categoria(cod, desc)

arvore_categoria = ArvoreBinaria()

def carregar_categorias():
    if os.path(ARQUIVOS_CATEGORIA):
        with open(ARQUIVOS_CATEGORIA, "r", Encoding="utf-8") as f:
            for linha in f:
                if linha.strip():
                    c = Categoria.from_linha(linha)
                    arvore_categoria.inserir(c.codigo_cat, c)

def salvar_categorias():
    salvar_tabela(arvore_categoria, ARQUIVOS_CATEGORIA, lambda c: c.to_linha())

def buscar_categoria(codigo):
    no = arvore_categoria.buscar(codigo)
    return no.valor if no else None

def cadastrar_categoria():
    print("\n --- Cadastro de Categoria de Gastos ---")
    try:
        cod = int(input("Código da Categoria: "))
    except ValueError:
        print("Erro: o código deve ser numérico!")
        return

    if buscar_categoria(cod):
        print("Erro: Categoria já cadastrada!")
        return

    desc = input("Descrição da Categoria: ").strip()
    if not desc:
        print("Erro: A descrição não pode ser vazia!")
        return

    categoria = Categoria(cod, desc)
    arvore_categoria.inserir(cod, categoria)
    salvar_categorias()
    print("Categoria cadastrada com sucesso!")

def listar_categoria():
    categoria = arvore_categoria.em_ordem()
    print("\n" + "=" * 45)
    print(f"{'Código':<8} _ {'Descrição':<32}")
    print("=" * 25)
    if not categoria:
        print("(nenhuma categoria cadastrada)")
    for c in categoria:
        print(f"{c.codigo_cat:<8} _ {c.descricao:<32}")
    print("=" * 45)

