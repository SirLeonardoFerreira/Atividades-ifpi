def main():
    populacao_aves = int(input("Digite o número da população de aves dodô: "))
    parada = populacao_aves * (10 / 100)
    ano = 1600
    while populacao_aves > parada:
        nascimento_aves = populacao_aves * (1 / 100)
        mortes_aves = populacao_aves * (6 / 100)
        populacao_aves += nascimento_aves - mortes_aves
        print(f'No ano de {ano}, o número de aves dodô que nasceram no ano foram {nascimento_aves:.0f}, o número de aves dodô mortas no ano foram {mortes_aves:.0f}, a população atual de aves dodô é {populacao_aves:.0f}.')
        ano += 1
if __name__ == '__main__':
    main()
