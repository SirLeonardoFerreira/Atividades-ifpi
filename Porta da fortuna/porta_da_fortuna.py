from random import *

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

Escolha uma porta (1, 2 ou 3):
''')

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
    print("Parabéns!")
else:
    print("Que peninha!")
