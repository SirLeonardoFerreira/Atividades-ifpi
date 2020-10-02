def ler_numeros(num):
    lista_numeros = []
    lista_par = []
    lista_impar = []
    for i in range(num):
        numero = int(input("Digite um número: "))
        lista_numeros.append(numero)
        if numero % 2 == 0:
          lista_par.append(numero)
        else: lista_impar.append(numero)
    return lista_numeros, lista_par, lista_impar
def main():
    resultado_lista_numeros, resultado_lista_par, resultado_lista_impar = ler_numeros(20)
    print(f'{resultado_lista_numeros}')
    print(f'{resultado_lista_par}')
    print(f'{resultado_lista_impar}')
if __name__ == '__main__':
    main()
