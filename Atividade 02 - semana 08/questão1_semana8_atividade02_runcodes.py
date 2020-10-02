def comprimento(n):
    return len(n)

def inverter(n):
    inverso = n[:]
    inverso.reverse()
    return inverso

def minimo(n):
    return min(n)

def maximo(n):
    return max(n)

def soma(n):
    return sum(n)

def main():
    lista = []
    while True:
        numero = int(input())
        if numero == 0: break
        lista.append(numero)
    print(f'{lista}')
    print(f'{comprimento(lista)}')
    print(f'{inverter(lista)}')
    print(f'{minimo(lista)}')
    print(f'{maximo(lista)}')
    print(f'{soma(lista)}')
if __name__ == '__main__':
    main()
