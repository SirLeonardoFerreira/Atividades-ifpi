def inveter_numero(num):
    resto = numero_invertido = 0
    while num > 0:
        resto = num % 10
        num //= 10
        numero_invertido = (numero_invertido * 10) + resto
    return numero_invertido

def main():
    numero = int(input("Digite um número inteiro: "))

    resultado_numero_invertido = inveter_numero(numero)

    print(f'O inverso do número {numero} é o número {resultado_numero_invertido}.')
if __name__ == '__main__':
    main()


    
