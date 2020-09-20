def media_idade(soma_idade, numero_pessoas):
    idade_media = soma_idade / numero_pessoas
    return idade_media

def main():
    numero_pessoas = soma_idade = menor_idade = maior_idade = 0

    while True:
        idade = int(input())
        if idade != 0:
            numero_pessoas += 1
            soma_idade += idade
            if numero_pessoas == 1:
                menor_idade = maior_idade = idade
            else:
                if menor_idade > idade:
                    menor_idade = idade
                elif maior_idade < idade:
                    maior_idade = idade

        if idade == 0: break

    if numero_pessoas != 0:
        resultado_media = media_idade(soma_idade, numero_pessoas)

        print(f'{numero_pessoas}')
        print(f'{resultado_media:.2f}')
        print(f'{menor_idade}')
        print(f'{maior_idade}')

if __name__ == '__main__':
    main()
