def consoante(v):
    if v.upper() in 'BCDFGHJKLMNPQRSTVWXYZ':
        return True
    else:
        return False

def main():
    caractere = input()

    resultado = consoante(caractere)

    print(f'{resultado}')

if __name__ == '__main__':
    main()

    
