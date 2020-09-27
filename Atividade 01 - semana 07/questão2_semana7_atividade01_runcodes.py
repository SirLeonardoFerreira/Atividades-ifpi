def compra_avista(preco):
    poupanca = 10000
    mes = 0
    while preco > poupanca:
        poupanca *= (1 + (0.7 / 100))
        preco *= (1 + (0.4 / 100))
        mes += 1
    return mes

def main():
    preco_carro = float(input())
    mes_total = compra_avista(preco_carro)
    print(f'{mes_total}')

if __name__ == '__main__':
    main()
