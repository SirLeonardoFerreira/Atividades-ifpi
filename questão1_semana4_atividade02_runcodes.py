def main():
    nome_pessoa = input()
    estado_civil = int(input())

    if estado_civil == 1:
        conjuge = input()
        caractere_total = len(nome_pessoa) + len(conjuge)
    else:
        caractere_total = len(nome_pessoa)

    print(f'{caractere_total}')

if __name__ == '__main__':
    main()
