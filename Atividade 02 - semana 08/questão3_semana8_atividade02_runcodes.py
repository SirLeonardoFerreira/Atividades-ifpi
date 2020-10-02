def ler_numeros_a(num):
    lista_numeros_a = []
    for i in range(num):
        numero = int(input())
        lista_numeros_a.append(numero)
    return lista_numeros_a

def ler_numeros_b(num):
    lista_numeros_b = []
    for i in range(num):
        numero = int(input())
        lista_numeros_b.append(numero)
    return lista_numeros_b

def ler_numeros_c(num_a, num_b):
    lista_numeros_c = []
    soma = aux_posicao = 0
    for elemento_a in num_a: 
        indice_a = num_a.index(elemento_a, aux_posicao)
        soma = elemento_a + num_b[indice_a]
        lista_numeros_c.append(soma)
        soma = 0
        aux_posicao += 1
        
    return lista_numeros_c
def main():
    resultado_lista_numeros_a = ler_numeros_a(20)
    resultado_lista_numeros_b = ler_numeros_b(20)
    resultado_lista_numeros_c = ler_numeros_c(resultado_lista_numeros_a, resultado_lista_numeros_b)
    print(f'{resultado_lista_numeros_a}')
    print(f'{resultado_lista_numeros_b}')
    print(f'{resultado_lista_numeros_c}')
if __name__ == '__main__':
    main()
