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
    populacao = int(input())
    cidades = carrega_cidades()
    print(f'CIDADES COM MAIS DE {populacao} HABITANTES:')
    for sigla, ibge, cidade, _, _, popu in cidades:
        if popu > populacao:
            print(f'IBGE: {ibge} - {cidade}({sigla}) - POPULAÇÃO: {popu}')
if __name__ == '__main__':
    main()
