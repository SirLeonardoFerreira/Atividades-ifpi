def vogal(a):
    return a.upper() in 'AEIOU'
        
def consoante(c):
    return c.upper() in 'BCDFGHJKLMNPQRSTVWXYZ'

def numero(x):
    return not x.upper() in 'AEIOU' and (not (x.upper() in 'BCDFGHJKLMNPQRSTVWXYZ') and  ('0' <= x <= '9'))

def mensagem(z):
    if vogal(z):
        return 'vogal'
    elif consoante(z):
        return 'consoante'
    elif numero(z):
        return 'número'
    else:
        return 'símbolo'
        
def main():
    caractere = input("Digite um caractere: ")
    resultado = mensagem(caractere)

    print(f'{resultado}')

if __name__ == '__main__':
    main()
