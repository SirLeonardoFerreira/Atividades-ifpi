def letra(x):
    if 'A' <= x <= 'Z' or 'a' <= x <= 'z':
        return True
    else:
        return False

def main():
    caractere_letra = input()
    resultado = letra(caractere_letra)

    print(f'{resultado}')

if __name__ == '__main__':
    main()
