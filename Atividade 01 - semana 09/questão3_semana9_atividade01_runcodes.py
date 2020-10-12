def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def main():
    dia = int(input())
    mes = int(input())
    cidades = carrega_cidades()
    if mes == 1:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE JANEIRO:')
    elif mes == 2:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE FEVEREIRO:')
    elif mes == 3:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE MARÇO:')
    elif mes == 4:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE ABRIL:')
    elif mes == 5:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE MAIO:')
    elif mes == 6:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE JUNHO:')
    elif mes == 7:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE JULHO:')
    elif mes == 8:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE AGOSTO:')
    elif mes == 9:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE SETEMBRO:')
    elif mes == 10:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE OUTUBRO:')
    elif mes == 11:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE NOVEMBRO:')
    elif mes == 12:
        print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE DEZEMBRO:')
    for sigla, _, cidade, d, m, _ in cidades:
        if d == dia and m == mes:
            print(f'{cidade}({sigla})')
if __name__ == '__main__':
    main()
