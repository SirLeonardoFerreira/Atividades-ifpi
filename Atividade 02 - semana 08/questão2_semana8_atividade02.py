def contador(n, valor):
    return n.count(valor)
def main():
    lista = []
    while True:
        numero = int(input("Digite um número (0 - FIM): "))
        if numero == 0: break
        lista.append(numero)
    numero_pesquisado = int(input("Digite um número da lista para ver quantas vezes ele foi digitado: "))
    print(f'{lista}')
    print(f'{numero_pesquisado}')
    print(f'{contador(lista, numero_pesquisado)}')
if __name__ == '__main__':
    main()
