from operator import itemgetter
def preence_dicionario():
    tempo_voltas = {}
    lista_voltas = []
    n = 0
    aux = 1
    aux_jogador = 1
    ranking = []
    while n < 6:
        jogador = input().strip()
        for c in range(10):
            voltas = float(input())
            lista_voltas.append(voltas)
            aux += 1
        tempo_voltas[jogador] = lista_voltas
        aux = 1
        n += 1
        aux_jogador += 1
        lista_voltas = []
    return tempo_voltas

def tempo_total(n):
    total = round(sum(n), 1)
    return total

def tempo_media_melhor(n):
    media = round(sum(n) / len(n) , 1)
    melhor_volta = round(min(n), 1)
    return [media, melhor_volta]
def main():
    dicionario_tempo_voltas = preence_dicionario()
    dicionario_tempo_total = {}
    dicionario_media_melhor = {}
    for cod in dicionario_tempo_voltas:
        resultado_total = tempo_total(dicionario_tempo_voltas[cod])
        dicionario_tempo_total[cod] = resultado_total
        lista_tempo = tempo_media_melhor(dicionario_tempo_voltas[cod])
        dicionario_media_melhor[cod] = lista_tempo

    ranking = sorted(dicionario_tempo_total.items(), key = itemgetter(1))
    print('-------|----------------------|---------------|---------------|---------------')
    print(' Ordem |   Nome do Corredor   |  Tempo Total  |  Tempo Médio  | Melhor Volta  ')
    print('-------|----------------------|---------------|---------------|---------------')
    for c, valor in enumerate(ranking):
        print(f'{c+1:^7}|{valor[0]:^22}|{valor[1]:^15}|{dicionario_media_melhor[valor[0]][0]:^15}|{dicionario_media_melhor[valor[0]][1]:^15}')
    print('-------|----------------------|---------------|---------------|---------------')
if __name__ == '__main__':
    main()
