def juros_poupanca(deposito, taxa):
    qtd_anos = 0
    rendimento_total = deposito
    while rendimento_total < 2 * deposito:
        rendimento = rendimento_total * (taxa / 100)
        rendimento_total += rendimento
        qtd_anos += 1
    return qtd_anos

def main():
    deposito_inicial = float(input("Digite o valor que você depositou: "))
    taxa_juros = float(input("Digite a taxa de juros anual: "))
    anos_dobro_deposito = juros_poupanca(deposito_inicial, taxa_juros)

    print(f'O deposito de {deposito_inicial:.2f} irá dobrar em {anos_dobro_deposito} anos.')
if __name__ == '__main__':
    main()
