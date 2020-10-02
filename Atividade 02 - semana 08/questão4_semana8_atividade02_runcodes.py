def ler_nomes(num):
    lista_nomes = []
    lista_altura = []
    for i in range(num):
        nomes = input()
        lista_nomes.append(nomes)
        numero = float(input())
        lista_altura.append(numero)
    return lista_nomes, lista_altura

def jogador_alto(lista_a, lista_b):
    indice_maior_altura = lista_b.index(max(lista_b))
    return indice_maior_altura

def media_altura(num):
    return sum(num) / len(num)
  
def main():
    resultado_ler_nomes, resultado_ler_altura = ler_nomes(12)
    resultado_jogador_alto = jogador_alto(resultado_ler_nomes, resultado_ler_altura)
    resultado_media_altura = media_altura(resultado_ler_altura)
    aux_posicao = 0
    print(f'JOGADOR MAIS ALTO DO TIME')
    print(f'{resultado_ler_nomes[resultado_jogador_alto]}')
    print(f'{resultado_ler_altura[resultado_jogador_alto]:.2f}')
    print(f'ALTURA MÉDIA DO TIME')
    print(f'{resultado_media_altura:.2f}')
    print(f'JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    for num in resultado_ler_altura:
        if num > resultado_media_altura:
            indice_maior_altura_media = resultado_ler_altura.index(num, aux_posicao)
            print(f'{resultado_ler_nomes[indice_maior_altura_media]}')
            print(f'{resultado_ler_altura[indice_maior_altura_media]:.2f}')
        aux_posicao += 1
if __name__ == '__main__':
    main()
