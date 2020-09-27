def numero_sorte(data):
    soma = 0
    while data > 0:
        soma += data % 10
        data //= 10
    return soma
def main():
    data_nascimento = int(input("Digite a sua data de nascimento nesse formato(ddmmaaaa): "))

    numero_da_sorte = numero_sorte(data_nascimento)
    print(f'O seu número da sorte é {numero_da_sorte}.')
if __name__ == '__main__':
    main()
