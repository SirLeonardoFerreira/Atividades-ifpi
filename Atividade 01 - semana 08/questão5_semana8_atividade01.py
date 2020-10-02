def ler_numeros_a(num):
    lista_numeros_a = []
    for i in range(num):
        numero = int(input("Digite os números da lista A: "))
        lista_numeros_a.append(numero)
    return lista_numeros_a

def ler_numeros_b(num):
    lista_numeros_b = []
    for i in range(num):
        numero = int(input("Digite os números da lista B: "))
        lista_numeros_b.append(numero)
    return lista_numeros_b

def ler_numeros_c(num_a, num_b):
    lista_numeros_c = []
    num_aux_a = 0
    num_aux_b = 1
    for elemento_a in num_a:
        lista_numeros_c.insert(num_aux_a, elemento_a)
        num_aux_a += 2
    for elemento_b in num_b:
        lista_numeros_c.insert(num_aux_b, elemento_b)
        num_aux_b += 2
    return lista_numeros_c

def main():
    resultado_lista_numeros_a = ler_numeros_a(25)
    resultado_lista_numeros_b = ler_numeros_b(25)
    resultado_lista_numeros_c = ler_numeros_c(resultado_lista_numeros_a, resultado_lista_numeros_b)
    print(f'{resultado_lista_numeros_a}')
    print(f'{resultado_lista_numeros_b}')
    print(f'{resultado_lista_numeros_c}')
if __name__ == '__main__':
    main()
