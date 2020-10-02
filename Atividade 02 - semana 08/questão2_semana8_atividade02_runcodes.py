def contador(n, valor):
    return n.count(valor)
def main():
    lista = []
    while True:
        numero = int(input())
        if numero == 0: break
        lista.append(numero)
    numero_pesquisado = int(input())
    print(f'{lista}')
    print(f'{numero_pesquisado}')
    print(f'{contador(lista, numero_pesquisado)}')
if __name__ == '__main__':
    main()
