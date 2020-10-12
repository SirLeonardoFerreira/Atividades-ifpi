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
    mes = int(input())
    populacao = int(input())
    cidades = carrega_cidades()
    if mes == 1:
        mes_aux = 'janeiro'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM JANEIRO:')
    elif mes == 2:
        mes_aux = 'fevereiro'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM FEVEREIRO:')
    elif mes == 3:
        mes_aux = 'março'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM MARÇO:')
    elif mes == 4:
        mes_aux = 'abril'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM ABRIL:')
    elif mes == 5:
        mes_aux = 'maio'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM MAIO:')
    elif mes == 6:
        mes_aux = 'junho'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM JUNHO:')
    elif mes == 7:
        mes_aux = 'julho'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM JULHO:')
    elif mes == 8:
        mes_aux = 'agosto'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM AGOSTO:')
    elif mes == 9:
        mes_aux = 'setembro'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM SETEMBRO:')
    elif mes == 10:
        mes_aux = 'outubro'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM OUTUBRO:')
    elif mes == 11:
        mes_aux = 'novembro'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM NOVEMBRO:')
    elif mes == 12:
        mes_aux = 'dezembro'
        print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM DEZEMBRO:')
    for sigla, _, cidade, d, m, popu in cidades:
        if popu > populacao and m == mes:
            print(f'{cidade}({sigla}) tem {popu} habitantes e faz aniversário em {d} de {mes_aux}.')
if __name__ == '__main__':
    main()
