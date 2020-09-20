def signo(dia, mes):
    if (21 <= dia <= 31 and mes == 3) or (1 <= dia <= 19 and mes == 4):
        return 'Áries'
    elif (20 <= dia <= 30 and mes == 4) or (1 <= dia <= 20 and mes == 5):
        return 'Touro'
    elif (21 <= dia <= 31 and mes == 5) or (1 <= dia <= 21 and mes == 6):
        return 'Gêmeos'
    elif (22 <= dia <= 30 and mes == 6) or (1 <= dia <= 22 and mes == 7):
        return 'Câncer'
    elif (23 <= dia <= 31 and mes == 7) or (1 <= dia <= 22 and mes == 8):
        return 'Leão'
    elif (23 <= dia <= 31 and mes == 8) or (1 <= dia <= 22 and mes == 9):
        return 'Virgem'
    elif (23 <= dia <= 30 and mes == 9) or (1 <= dia <= 22 and mes == 10):
        return 'Libra'
    elif (23 <= dia <= 31 and mes == 10) or (1 <= dia <= 21 and mes == 11):
        return 'Escorpião'
    elif (22 <= dia <= 30 and mes == 11) or (1 <= dia <= 21 and mes == 12):
        return 'Sagitário'
    elif (22 <= dia <= 31 and mes == 12) or (1 <= dia <= 19 and mes == 1):
        return 'Capricórnio'
    elif (20 <= dia <= 31 and mes == 1) or (1 <= dia <= 18 and mes == 2):
        return 'Aquário'
    elif (19 <= dia <= 29 and mes == 2) or (1 <= dia <= 20 and mes == 3):
        return 'Peixes'

def main():
    dia_nascimento = int(input("Digite o dia em que você nasceu: "))
    mes_nascimento = int(input("Digite o mês em que você nasceu: "))
    ano_nascimento = int(input("Digite o ano em que você nasceu: "))

    mensagem_signo = signo(dia_nascimento, mes_nascimento)

    print(f'O seu signo é {mensagem_signo}')

if __name__=='__main__':
    main()
