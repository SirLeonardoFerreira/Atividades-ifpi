def media_numeros(soma, qtd):
    media = soma / qtd
    return media

def main():
    soma_numeros = 0
    qtd_numeros = 0
    while True:
        numeros_inteiro = int(input())
        if numeros_inteiro != 0:
            soma_numeros += numeros_inteiro
            qtd_numeros += 1
        if numeros_inteiro == 0: break

    if soma_numeros != 0:
        resultado_media = media_numeros(soma_numeros, qtd_numeros)    
        print(f'{resultado_media:.2f}')



if __name__ == '__main__':
    main()
