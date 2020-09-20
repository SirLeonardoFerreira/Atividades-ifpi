def impar(x):
    return x % 2 != 0

def main():
    numero = int(input())
    resultado = impar(numero)

    if resultado:
        print(True)

    else:
        print(False)

if __name__ == '__main__':
    main()
