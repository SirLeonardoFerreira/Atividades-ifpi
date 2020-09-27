def compra_avista(preco):
    poupanca = 10000
    mes = 0
    while preco > poupanca:
        poupanca *= (1 + (0.7 / 100))
        preco *= (1 + (0.4 / 100))
        mes += 1
    return mes

def main():
    preco_carro = float(input("Digite o preço que o carro custa hoje: "))
    mes_total = compra_avista(preco_carro)
    print(f'O carro poderá ser comprado á vista em {mes_total} meses.')

if __name__ == '__main__':
    main()
