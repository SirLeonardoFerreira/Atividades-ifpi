def media_idade(soma_idade, numero_pessoas):
    idade_media = soma_idade / numero_pessoas
    return idade_media

def main():
    numero_pessoas = soma_idade = menor_idade = maior_idade = 0

    while True:
        idade = int(input("Digite a idade da pessoa: "))
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

        print(f'Apareceram {numero_pessoas} pessoas no dia de hoje.')
        print(f'A idade média das pessoas de hoje foram {resultado_media:.2f} anos.')
        print(f'A maior idade é {maior_idade} anos e a menor idade é {menor_idade} anos.')

if __name__ == '__main__':
    main()
