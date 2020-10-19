def main():
    dicionario_dado = {}
    qtd_jogada = qtd_face_um = qtd_face_dois = qtd_face_tres = qtd_face_quatro = qtd_face_cinco = qtd_face_seis = 0
    while True:
        resultado_dado = int(input("Digite o resultado que saiu ao jogar o dado(0 - encerra): "))
        if resultado_dado == 1:
            qtd_face_um += 1
            qtd_jogada += 1
        elif resultado_dado == 2:
            qtd_face_dois += 1
            qtd_jogada += 1
        elif resultado_dado == 3:
            qtd_face_tres += 1
            qtd_jogada += 1
        elif resultado_dado == 4:
            qtd_face_quatro += 1
            qtd_jogada += 1
        elif resultado_dado == 5:
            qtd_face_cinco += 1
            qtd_jogada += 1
        elif resultado_dado == 6:
            qtd_face_seis += 1
            qtd_jogada += 1
        elif resultado_dado == 0: break
    dicionario_dado['face 1'] = qtd_face_um
    dicionario_dado['face 2'] = qtd_face_dois
    dicionario_dado['face 3'] = qtd_face_tres
    dicionario_dado['face 4'] = qtd_face_quatro
    dicionario_dado['face 5'] = qtd_face_cinco
    dicionario_dado['face 6'] = qtd_face_seis

    print(f'O dado foi lançado {qtd_jogada} vezes.')
    for cod in dicionario_dado:
        print(f'A {cod} saiu {dicionario_dado[cod]} vezes.')
if __name__ == '__main__':
    main()
