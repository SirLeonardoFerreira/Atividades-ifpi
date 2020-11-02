from operator import itemgetter
def carregar_arquivos(arq):
    linhas = []
    with open(arq) as f:
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

def formatar_data(linha):
    meses = (
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
        )
    d, m, a = linha['dia'], linha['mes'], linha['ano']
    return f'{d:0>2d} de {meses[m - 1]} de {a}'

def menor_fechamento(arq):
    ordenado = sorted(arq, key = itemgetter('fechamento'))
    return ordenado[0]['fechamento'], formatar_data(ordenado[0])

def main():
    arquivo = input()
    empresa = carregar_arquivos(arquivo)
    fechamento_menor, data = menor_fechamento(empresa)
    print(f'O menor preço no fechamento foi {fechamento_menor:.2f} em {data}')

if __name__ == '__main__':
    main()
