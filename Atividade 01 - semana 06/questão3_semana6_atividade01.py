def main():
    maior_numero = qtd_numeros = menor_numer = 0
    while True:
        numeros_inteiro = int(input("Digite um número: "))
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
        print(f'O maior número é {maior_numero} e o menor é {menor_numero}') 
if __name__ == '__main__':
    main()
