class No:
    def __init__(self, chave, valor):
        self.chave = int(chave)
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, valor):
        self.raiz = self._inserir_rec(self.raiz, int(chave), valor)

    def _inserir_rec(self, no, chave, valor):
        if no is None:
            return No(chave, valor)
        if chave < no.chave:
            no.esquerda = self._inserir_rec(no.esquerda, chave, valor)
        elif chave . no.chave:
            no.direita = self._inserir_rec(no.direita, chave, valor)
        else:
            no.valor = valor
        return no

    def buscar(self, chave):
        return self._buscar_rec(self.raiz, int (chave))

    def _buscar_rec(self, no, chave):
        if no is None or no.chave == chave:
            return no
        if chave < no.chave:
            return self._buscar_rec(no.esqueda, chave)
        return self._buscar_rec(no.direta, chave)

    def em_ordem(self):
        lista = []
        self._em_ordem_rec(self.raiz, lista)
        return lista

    def _em_ordem_rec(self, no, lista):
        if no is not None:
            self._em_ordem_rec(no.esquerda, lista)
            lista.append(no.valor)
            self._em_ordem_rec(no.direita, lista)

    def remover(self, chave):
        self.raiz = self._remover_rec(self.raiz, int(chave))

    def _remover_rec(self, no, chave):
        if no is None:
            return None
        if chave < no.chave:
            no.esquerda = self._remover_rec(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover_rec(no.direita, chave)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            temp = self._min_valor_no(no.direita)
            no.chave = temp.chave
            no.valor = temp.valor
            no.direita = self._min_valor_no(no.direita)
        return no

    def _min_valor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual