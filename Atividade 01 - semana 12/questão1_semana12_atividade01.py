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

def maior_abertura(arq):
    ordenado = sorted(arq, key = itemgetter('abertura'))
    return ordenado[-1]['abertura'], formatar_data(ordenado[-1])

def main():
    arquivo = input()
    empresa = carregar_arquivos(arquivo)
    abertura_maior, data = maior_abertura(empresa)
    print(f'O maior preço na abertura foi {abertura_maior:.2f} em {data}')

if __name__ == '__main__':
    main()
