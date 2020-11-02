from operator import itemgetter
def carregar_arquivos(arq):
    linhas = []
    with open(arq.strip('\r')) as f:
        f.readline()
        for linha in f.readlines():
            data, abertura, alta, baixa, fechamento, volume = linha.strip().split(',')
            ano, mes, dia = data.split('-')
            linhas.append(
                {
                    'ano': int(ano),
                    'mes': int(mes),
                    'dia': int(dia),
                    'abertura': float(abertura),
                    'alta': float(alta),
                    'baixa': float(baixa),
                    'fechamento': float(fechamento),
                    'volume': int(volume),
                }
            )
    return linhas

def variacao_preco(arq, m, a):
    lista_dia = []
    for valor in arq:
        if valor['mes'] == m and valor['ano'] == a:
            if valor['abertura'] > valor['fechamento']:
                variacao = round(valor['abertura'] - valor['fechamento'], 2)
                lista_dia.append(
                    {
                        'dia': valor['dia'],
                        'abertura': valor['abertura'],
                        'fechamento': valor['fechamento'],
                        'variacao': variacao
                    }
                )
    return lista_dia

def main():
    arquivo = input()
    mes = int(input())
    ano = int(input())
    empresa = carregar_arquivos(arquivo)
    dias_varicao = variacao_preco(empresa, mes, ano)
    ordenado = sorted(dias_varicao, key = itemgetter('dia'))
    print(f'Dias de {mes}/{ano} que houve queda no preço da ação:')
    for indice in ordenado:
        if indice['dia'] < 10:
            if mes < 10:
                data = f"'0{indice['dia']}/0{mes}/{ano}'"
            else:
                data = f"'0{indice['dia']}/{mes}/{ano}'"
        else:
            if mes < 10:
                data = f"'{indice['dia']}/0{mes}/{ano}'"
            else:
                data = f"'{indice['dia']}/{mes}/{ano}'"
        print(f'({data}, {indice["abertura"]}, {indice["fechamento"]}, {indice["variacao"]})')

if __name__ == '__main__':
    main()
