def alcanca_tartaruga(distancia_tartaruga):
    distancia_lebre = tempo = 0
    while distancia_tartaruga > distancia_lebre:
        distancia_tartaruga += 1
        distancia_lebre += 10
        tempo += 1
    return tempo
def main():
    distancia_tartaruga = int(input())
    
    tempo_total = alcanca_tartaruga(distancia_tartaruga)
    print(f'{tempo_total}')


if __name__ == '__main__':
    main()
