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
