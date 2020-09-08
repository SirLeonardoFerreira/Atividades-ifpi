def e_par(n):
    return n % 2 == 0

def numeros_pares(inicio, quantidade):
    if e_par(inicio):
        inicio += 2
    else:
        inicio += 1

    numeros_pares = ' '
    for n in range(inicio, inicio + (quantidade * 2), 2):
        numeros_pares += str(n) + ' '

    return numeros_pares.strip()

def main():
    num_inicio = int(input("Início do intervalo: "))
    qtd = int(input("Quantidade de números pares: "))
    print(f'{qtd} pares após {num_inicio}: ')
    print(numeros_pares(num_inicio, qtd))

if __name__ == '__main__':
    main()
