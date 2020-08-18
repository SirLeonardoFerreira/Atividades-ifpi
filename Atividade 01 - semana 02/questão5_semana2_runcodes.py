def compra(desconto):
    a_vista = desconto * 0.91
    prazo_cinco = (desconto) / 5
    prazo_dez = (desconto * 1.17) / 10
    return a_vista, prazo_cinco, prazo_dez

def main():
    valor_compra = float(input())
    a_vista, prazo_cinco, prazo_dez = compra(valor_compra)
    print(f'{a_vista:.2f}')
    print(f'{prazo_cinco:.2f}')
    print(f'{prazo_dez:.2f}')

if __name__ == '__main__':
    main()

    
