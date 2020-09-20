def compra(desconto):
    a_vista = desconto * 0.91
    prazo_cinco = (desconto) / 5
    prazo_dez = (desconto * 1.17) / 10
    return a_vista, prazo_cinco, prazo_dez

def main():
    valor_compra = float(input("Digite o valor da compra: "))
    a_vista, prazo_cinco, prazo_dez = compra(valor_compra)
    print(f'O valor para pagamento á vista é: R${a_vista:.2f} reais, o valor da prestação em 5 vezes é: R${prazo_cinco:.2f} reais e o valor da prestação em 10 vezes é: R${prazo_dez:.2f} reais.')

if __name__ == '__main__':
    main()

    
