def main():
    nome_pessoa = input("Digite o seu nome: ")
    estado_civil = input("Digite o seu estado civil - Considere C - casado e S - solteiro: ")

    if estado_civil.upper() == 'C':
        conjuge = input("Digite o nome do seu cônjuge: ")
        caractere_total = len(nome_pessoa) + len(conjuge)
    else:
        caractere_total = len(nome_pessoa)

    print(f'No(s) nome(s) existem {caractere_total} carectéres')

if __name__ == '__main__':
    main()
