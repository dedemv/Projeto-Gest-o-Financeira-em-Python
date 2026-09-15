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
        return

arvore_pessoas = ArvoreBinaria()

def carregar_pessoas():
    