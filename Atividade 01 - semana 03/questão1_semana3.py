def sexo(x):
    if x == 1:
        return 'Ilmo Sr.'

    else:
        return 'Ilma Sra.'

def main():
    nome = input("Digite o seu nome: ")
    sexo_informado = int(input("Digite o seu sexo: (1 - Masculino ou 2 - Feminino) "))

    mensagem_sexo = sexo(sexo_informado)

    print(f'{mensagem_sexo} {nome}')

if __name__ == '__main__':
    main()
