def main():
    numero = 1
    soma = 0
    while True:
        if numero != 0:
            numero = int(input())
            soma += numero

        if numero == 0: break

    print(f'{soma}')

if __name__ == '__main__':
    main()
