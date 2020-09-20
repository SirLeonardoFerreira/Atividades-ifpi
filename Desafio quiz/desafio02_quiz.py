def main():
    print('''
    Qual foi o jogador que marcou os dois do campeão da libertadores de 2019?
    a - Gabigordo(sósia)
    b - Gabigol
    c - Gabriel jamal
    ''')
    resultado = input()

    if resultado.lower() == 'a':
        print("Errado, esse não faz gol nem no muralha!")
    elif resultado.lower() == 'b':
        print("Certa resposta, Gabigol o artilheiro da Ámerica.")
    elif resultado.lower() == 'c':
        print("Brincadeira! Esse pereba nem no flamengo está mais.")

    else:
        print("Você não escolheu nenhuma das opções acimas")

if __name__ == '__main__':
    main()

    
