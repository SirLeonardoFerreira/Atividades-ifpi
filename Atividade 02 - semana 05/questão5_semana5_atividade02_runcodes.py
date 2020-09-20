def prestacao(valor_compra, parcela):
    valor_prest = valor_compra / (parcela + 1)
    return valor_prest
    
def main():
    valor_compra = int(input())
    valor_parcela = 24
    for parcela in range(valor_parcela):
        valor_prestacao = prestacao(valor_compra, parcela)
        print(f'{parcela + 1}x de R$ {valor_prestacao:.2f}')
        

    
if __name__ == '__main__':
    main()
