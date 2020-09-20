def nome(a):
    return len(a)
def main():
    nome_x = input("Digite o seu nome: ")
    nome_x2 = nome(nome_x)
    print(f'Possui {nome_x2} caracteres')

if __name__ == '__main__':
    main()
