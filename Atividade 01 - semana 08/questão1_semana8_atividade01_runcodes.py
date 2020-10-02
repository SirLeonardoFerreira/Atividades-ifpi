def ler_numeros(n):
    numeros = []
    for num in range(n):
        numeros.append(int(input()))
    return numeros

def soma_numeros(numeros):
    return sum(numeros)

def multiplicacao_numeros(numeros):
    produto_numeros = 1
    for num in numeros:
        produto_numeros *= num
    return produto_numeros
def main():
    numeros = ler_numeros(10)
    soma = soma_numeros(numeros)
    multiplicacao = multiplicacao_numeros(numeros)
    print(f'{numeros}')
    print(f'{soma}')
    print(f'{multiplicacao}')

if __name__ == '__main__':
    main()
