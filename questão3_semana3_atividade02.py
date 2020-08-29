def consoante(v):
    if v.upper() in 'BCDFGHJKLMNPQRSTVWXYZ':
        return True
    else:
        return False

def main():
    caractere = input("Digite um caractere: ")

    resultado = consoante(caractere)

    print(f'{resultado}')

if __name__ == '__main__':
    main()

    
