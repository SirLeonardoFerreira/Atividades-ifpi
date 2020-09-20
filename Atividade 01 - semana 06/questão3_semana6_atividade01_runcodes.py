def main():
    maior_numero = 0
    menor_numero = 0
    qtd_numeros = 0
    while True:
        numeros_inteiro = int(input())
        if numeros_inteiro != 0:
            qtd_numeros += 1
            if qtd_numeros == 1:
                maior_numero = numeros_inteiro
                menor_numero = numeros_inteiro
            else:
                if numeros_inteiro > maior_numero:
                   maior_numero = numeros_inteiro
                elif numeros_inteiro < menor_numero:
                   menor_numero = numeros_inteiro 
        if numeros_inteiro == 0: break

    if qtd_numeros != 0:
        print(f'{maior_numero}')
        print(f'{menor_numero}') 
if __name__ == '__main__':
    main()
