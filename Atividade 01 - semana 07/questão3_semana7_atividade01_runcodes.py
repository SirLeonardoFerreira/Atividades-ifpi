def natalidade (populacao_a, populacao_b):
    tempo = 0
    while populacao_a > populacao_b:
        populacao_a *= (1 + (2 / 100))
        populacao_b *= (1 + (3 / 100))
        tempo += 1
    return tempo
def main():
    populacao_um = int(input())
    populacao_dois = int(input())
    
    if populacao_um > populacao_dois:
        populacao_a = populacao_um
        populacao_b = populacao_dois
    else:
        populacao_a = populacao_dois
        populacao_b = populacao_um
        
    tempo_total = natalidade (populacao_a, populacao_b)
    
    print(f'{tempo_total}')
if __name__ == '__main__':
    main()
