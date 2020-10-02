def gerar_numeros(n):
    lista_zerada = []
    lista = []
    for num in range(n):
        lista_zerada.append(0)
        lista.append(num + 1)
    return lista_zerada, lista

def proximo_numeros(num):
    numeros_lidos = []
    for i in range(num):
        numero = int(input())
        numeros_lidos.append(numero)
    return numeros_lidos

def numero_inverso(num):
    inverso = []
    for i in range(num):
        numero = int(input())
        inverso.insert(0, numero)
    return inverso

def main():
    
    numero_lido = int(input())
    resultado_zerado, resultado_lista = gerar_numeros(numero_lido)
    resultado_numeros_lidos = proximo_numeros(numero_lido)
    resutado_numero_inverso = numero_inverso(numero_lido)
    print(resultado_zerado)
    print(resultado_lista)
    print(resultado_numeros_lidos)
    print(resutado_numero_inverso)
    
if __name__ == '__main__':
    main()
