from random import *

#o usuário muda esta variável para terminar o jogo
score = 0
jogando = True

#imprima as o nome e as instruções do jogo

print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos
''')
#repetir, enquanto a variável 'jogando' estiver com valor 'True' (verdadeiro)

while jogando == True:
    #escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 10)
    proximo_numero = randint(1,10)

    #mostra ao jogador o número sorteado
    print(f'Seu próximo número é {proximo_numero}.')

    #mostra ao jogador a sua pontuação atual
    score += proximo_numero
    print(f'Sua pontuação agora é {score}.')

    #pergunte ao jogador se ele quer continuar jogando
    print("\nGostaria de somar mais um número? (s/n)")
    resposta = input().lower()

    #termina o jogo se o jogador digita 'n'
    if resposta == 'n' or resposta == 'nao':
        jogando = False

# mostra se o jogador conseguiu somar 21 pontos
if score == 21:
    print(f'Parabéns! Você conseguiu somar 21 pontos.')

else:
    print(f'Que pena! A sua pontuação final foi {score}.')
