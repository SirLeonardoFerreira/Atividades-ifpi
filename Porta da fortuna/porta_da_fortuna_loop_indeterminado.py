from random import *

#o usuário muda esta variável para terminar o jogo
jogando = True

score = 0

#imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna!

=========

Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!

  ________   ________  ________
 |        | |        ||        |
 |   [1]  | |  [2]   ||  [3]   |
 |      ° | |     °  ||     °  |
 |________| |________||________|

''')

#repetir, enquanto a variável 'jogando' estiver com valor 'True' (verdadeiro)

while jogando == True:
    print("\nEscolha uma porta (1, 2 ou 3):")

    #pegue a porta escolhida e a armazene como um número inteiro (int)
    porta_escolhida = input()
    porta_escolhida = int(porta_escolhida)

    #escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)
    porta_certa = randint(1,3)

    #mostre ao jogador qual porta ele escolheu e qual era a porta certa
    print("A porta escolhida foi a", porta_escolhida)
    print("A porta certa é a", porta_certa)

    #o jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo
    if porta_escolhida == porta_certa:
        score += 1
        print("Parabéns!")
    else:
        print("Que peninha!")
    print(f'A sua pontuação foi {score} pontos.')

    #pergunte ao jogador se ele quer continuar jogando
    print("\nVocê quer jogar de novo? (s/n)")
    resposta = input()

    #termina o jogo se o jogador digita 'n'
    if resposta == 'n':
        jogando = False

print("Obrigado por jogar.")
print("Sua pontuação final é de", score)
