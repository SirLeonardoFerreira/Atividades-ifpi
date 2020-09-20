def digito_impar(digito):
    dezena = digito // 10
    unidade = (digito % 10)
    if dezena % 2 != 0:
        dezena = 1
    else:
        dezena = 0

    if unidade % 2 != 0:
        unidade = 1
    else:
        unidade = 0

    quanti_par = dezena + unidade
    if quanti_par == 0:
        return 'Nenhum dígito é ímpar.'
    elif quanti_par == 1:
        return 'Apenas um dígito é ímpar.'
    elif quanti_par == 2:
        return 'Os dois dígitos são ímpares.'
    

def main():
    numero = int(input())

    if 10 <= numero <= 99:
       mensagem = digito_impar(numero)
       print(f'{mensagem}')
    else:
        'erro'

if __name__ == '__main__':
    main()
