def alcanca_tartaruga(distancia_tartaruga):
    distancia_lebre = tempo = 0
    while distancia_tartaruga > distancia_lebre:
        distancia_tartaruga += 1
        distancia_lebre += 10
        tempo += 1
    return tempo
def main():
    distancia_tartaruga = int(input("Digite quantos metros a tartaruga tem de vantagem: "))
    
    tempo_total = alcanca_tartaruga(distancia_tartaruga)
    print(f'A lebre vai alcançar a tartaruga em {tempo_total} minutos.')


if __name__ == '__main__':
    main()
