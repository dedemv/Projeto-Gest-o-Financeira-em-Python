# para salvar a arvore em um txt

#percorre a arvore em ordem e grava cada item
def salvar_tabela(arvore, nome_arquivo, formato_func):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for item in arvore.em_ordem():
            f.write(formato_func(item) + "\n")