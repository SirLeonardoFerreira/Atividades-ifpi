def ler_numeros(n):
    numeros = []
    for num in range(n):
        numeros.append(int(input("Digite um número inteiro: ")))
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
    print(f'Os números que compõem a lista são: {numeros}')
    print(f'A soma dos números que compõem a lista é {soma}')
    print(f'O produto dos números que compõem a lista é {multiplicacao}')

if __name__ == '__main__':
    main()
