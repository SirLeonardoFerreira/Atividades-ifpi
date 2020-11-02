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

def volume_medio(arq, m, a):
    soma_volume = qtd = 0
    for valor in arq:
        if valor['mes'] == m and valor['ano'] == a:
            soma_volume += valor['volume']
            qtd += 1
    return round(soma_volume / qtd, )

def main():
    arquivo = input()
    mes = int(input())
    ano = int(input())
    empresa = carregar_arquivos(arquivo)
    media_volume = volume_medio(empresa, mes, ano)
    print(f'O volume médio em {mes}/{ano} foi {media_volume}')

if __name__ == '__main__':
    main()
