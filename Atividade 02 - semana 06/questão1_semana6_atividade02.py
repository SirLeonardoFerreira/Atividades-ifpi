def main():
    numero = 1
    soma = 0
    while True:
        if numero != 0:
            numero = int(input("Digite um número: "))
            soma += numero

        if numero == 0: break

    print(f'A soma dos números digitados é {soma}.')

if __name__ == '__main__':
    main()
