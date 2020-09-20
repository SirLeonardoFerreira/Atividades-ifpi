def inveter_numero(num):
    resto = 0
    numero_invertido = 0
    while num > 0:
        resto = num % 10
        num //= 10
        numero_invertido = (numero_invertido * 10) + resto
    return numero_invertido

def main():
    numero = int(input())

    resultado_numero_invertido = inveter_numero(numero)

    print(f'{resultado_numero_invertido}')
if __name__ == '__main__':
    main()


    
