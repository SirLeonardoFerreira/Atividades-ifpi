def vogal(v):
    if v.upper() in 'AEIOU':
        return True
    else:
        return False

def main():
    caractere = input()

    resultado = vogal(caractere)

    print(f'{resultado}')

if __name__ == '__main__':
    main()

    
