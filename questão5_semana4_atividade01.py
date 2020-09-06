def imc(massa, altura):
    return massa / (altura ** 2)
def mensagem(imc_x):
    if imc_x < 18.5:
        return 'Abaixo do peso'
    elif 18.5 < imc_x < 25:
        return 'Peso normal'
    elif 25 < imc_x < 30:
        return 'Sobrepeso'
    elif 30 < imc_x < 35:
        return 'Obeso leve'
    elif 35 < imc_x < 40:
        return 'Obeso moderado'
    else:
        return 'Obeso mórbido'

def main ():
    peso_massa = float(input("Digite o seu peso: "))
    altura_metro = float(input("Digite a sua altura: "))

    imc_pessoa = imc(peso_massa, altura_metro)
    mensagem_imc = mensagem(imc_pessoa)

    print(f'O seu imc é {imc_pessoa:.2f}')
    print(f'A classificação do seu imc é {mensagem_imc}')

if __name__ == '__main__':
    main()
