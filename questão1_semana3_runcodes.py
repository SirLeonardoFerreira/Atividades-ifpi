def sexo(x):
    if x == 1:
        return 'Ilmo Sr.'

    else:
        return 'Ilma Sra.'

def main():
    nome = input()
    sexo_informado = int(input())

    mensagem_sexo = sexo(sexo_informado)

    print(f'{mensagem_sexo} {nome}')

if __name__ == '__main__':
    main()
