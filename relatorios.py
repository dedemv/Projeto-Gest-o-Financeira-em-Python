from categoria import buscar_categoria
from banco import buscar_banco
from pessoa import buscar_pessoa
from conta import arvore_contas, buscar_contas
from transacao import arvore_transacoes

def relatorio_transacoes_periodo():
    print("\n--- Relatório de transações por Período ---")
    data_inicio = input("Data Inicial (AAAA-MM-DD): ").strip()
    data_fim = input("Data Final (AAAA-MM-DD): ").strip()

    todas = arvore_transacoes.em_ordem()
    saldo_periodo = 0.0
    encontrou = False

    print("\n" + "=" * 85)
    print(f"{'ID':<6} _ {'Data':<10} _ {'Categoria':<20} _ {'Banco':<20} _ {"Tipo":<7} _ {'Valor (R$)':<10}")
    print("=" * 85)

    for t in todas:
        if data_inicio <= t.data <= data_fim:
            encontrou = True

            categoria = buscar_categoria(t.cod_cat)
            desc_cat = categoria.descricao if categoria else "N/A"

            conta = buscar_contas(t.cod_conta)
            nome_banco = "N/A"
            if conta:
                banco = buscar_banco(conta.cod_banco)
                if banco:
                    nome_banco = banco.descricao

            if t.debito_credito == "C":
                saldo_periodo += t.valor
                tipo = "Crédito"
            else:
                saldo_periodo -= t.valor
                tipo = "Débito"
            print(f"{t.codigo_trans:<6} _ {t.data:<10} _ {desc_cat:<20} _ {nome_banco:20} _ {tipo:<7} _ R$ {t.valor:9.2f}")

    print("=" * 85)
    if not encontrou:
        print("Nenhuma transação encontrada no periodo informado.")
    print(f"SALDO DAS TRANSAÇÕES NO PERÍODO: R$ {saldo_periodo:.2f}\n")

def relatorio_saldos_contas():
    print("\n --- Relatório de Saldos de Contas ---")
    contas = arvore_contas.em_ordem()
    saldo_geral = 0.0

    print("\n" + "=" * 80)
    print(f"{'Cod':<5} | {'Descrição Conta':<20} | {'Banco':<20} | {'Titular':<20} | {'Saldo':<10}")
    print("=" * 80) 

    for c in contas: 
        banco = buscar_banco(c.cod_banco)
        nome_banco = banco.descricao if banco else "N/A"

        pessoa = buscar_pessoa(c.cod_pessoa)
        nome_pessoa = pessoa.nome if pessoa else "N/A"

        saldo_geral += c.saldo

        print(f"{c.cod_conta:<5} | {c.descricao:<20} | {nome_banco:<20} | {nome_pessoa:<20} | R$ {c.saldo:<9.2f}")
    print("=" * 80)
    print(f"SALDO GERAL (SOMATÓRIO DE TODAS AS CONTAS): R$ {saldo_geral:.2f}\n")