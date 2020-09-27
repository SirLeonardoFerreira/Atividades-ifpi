def main():
    populacao_aves = int(input())
    parada = populacao_aves * (10 / 100)
    ano = 1600
    while populacao_aves > parada:
        nascimento_aves = populacao_aves * (1 / 100)
        mortes_aves = populacao_aves * (6 / 100)
        populacao_aves += nascimento_aves - mortes_aves
        print(f'{ano},{nascimento_aves:.0f},{mortes_aves:.0f},{populacao_aves:.0f}')
        ano += 1
if __name__ == '__main__':
    main()
