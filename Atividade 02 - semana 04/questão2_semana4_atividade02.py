def digito_par(digito):
    centena = digito // 100
    dezena = (digito % 100) // 10
    unidade = ((digito % 100) % 10)
    if (centena % 2) == 0:
        centena = 1
    else:
        centena = 0
    if dezena % 2 == 0:
        dezena = 1
    else:
        dezena = 0

    if unidade % 2 == 0:
        unidade = 1
    else:
        unidade = 0

    quanti_par = centena + dezena + unidade
    return quanti_par

def main():
    numero = int(input("Digite um número entre 100 e 999: "))

    if 100 <= numero <= 999:
       resultado = digito_par(numero)
       print(f'O número {numero} tem {resultado} dígitos pares')
    else:
        'erro'

if __name__ == '__main__':
    main()
    
