def juros_poupanca(deposito, taxa):
    qtd_anos = 0
    rendimento_total = deposito
    while rendimento_total < 2 * deposito:
        rendimento = rendimento_total * (taxa / 100)
        rendimento_total += rendimento
        qtd_anos += 1
    return qtd_anos

def main():
    deposito_inicial = float(input())
    taxa_juros = float(input())
    anos_dobro_deposito = juros_poupanca(deposito_inicial, taxa_juros)

    print(f'{anos_dobro_deposito}')
if __name__ == '__main__':
    main()
