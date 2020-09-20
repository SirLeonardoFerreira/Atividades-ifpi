def divida_maior(salario, divida):
    mes = 11
    ano = 2016
    while True:
        if salario > divida:
            if mes == 3:
                salario *= (1 + (5 / 100))
                divida *= (1 + (15 / 100))
                mes += 1

            elif mes != 3:
                divida *= (1 + (15 / 100))
                if divida < salario:
                    if mes == 12:
                        mes = 1
                        ano += 1
                    else:
                        mes += 1
        if salario < divida: break
    return mes, ano
def main():
    salario = float(input())
    divida = float(input())
        
    mes_final, ano_final = divida_maior(salario, divida)
    print(f'{mes_final}/{ano_final}')

if __name__ == '__main__':
    main()
