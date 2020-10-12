from random import randint, seed
seed()
def gerar_matriz(linhas, colunas):
    matriz = [['Fabricante / Ano', 2013, 2014, 2015, 2016, 2017, 2018], ['Fiat', 0, 0, 0, 0, 0, 0], ['Ford', 0, 0, 0, 0, 0, 0], ['GM', 0, 0, 0, 0, 0, 0], ['Wolkswagen', 0, 0, 0, 0, 0, 0]]
    for l in range(linhas):
        for c in range(colunas):
            if l > 0 and c > 0:
                matriz[l][c] = int(input("Digite o número de vendas:"))
            
    return matriz

def volume_maior(lista):
    volume_vendas_primeiro = lista[1][1] + lista[2][1] + lista[3][1] + lista[4][1]
    ano_vendas_primeira = 2013
    volume_vendas_segundo = lista[1][2] + lista[2][2] + lista[3][2] + lista[4][2]
    ano_vendas_segundo = 2014
    volume_vendas_terceiro = lista[1][3] + lista[2][3] + lista[3][3] + lista[4][3]
    ano_vendas_terceiro = 2015
    volume_vendas_quarto = lista[1][4] + lista[2][4] + lista[3][4] + lista[4][4]
    ano_vendas_quarto = 2016
    volume_vendas_quinto = lista[1][5] + lista[2][5] + lista[3][5] + lista[4][5]
    ano_vendas_quinto = 2017
    volume_vendas_sexto = lista[1][6] + lista[2][6] + lista[3][6] + lista[4][6]
    ano_vendas_sexto = 2018
    lista_maior_volume = [volume_vendas_primeiro, volume_vendas_segundo, volume_vendas_terceiro, volume_vendas_quarto, volume_vendas_quinto, volume_vendas_sexto]
    maior_volume = max(lista_maior_volume, key = int)
    if maior_volume == volume_vendas_primeiro:
        ano_maior_volume = ano_vendas_primeira
    elif maior_volume == volume_vendas_segundo:
        ano_maior_volume = ano_vendas_segundo
    elif maior_volume == volume_vendas_terceiro:
        ano_maior_volume = ano_vendas_terceiro
    elif maior_volume == volume_vendas_quarto:
        ano_maior_volume = ano_vendas_quarto
    elif maior_volume == volume_vendas_quinto:
        ano_maior_volume = ano_vendas_quinto
    elif maior_volume == volume_vendas_sexto:
        ano_maior_volume = ano_vendas_sexto
    return maior_volume, ano_maior_volume

def volume_media(lista):
    media_fiat = (lista[1][1] + lista[1][2] + lista[1][3] + lista[1][4] + lista[1][5] + lista[1][6]) / 6
    media_ford = (lista[2][1] + lista[2][2] + lista[2][3] + lista[2][4] + lista[2][5] + lista[2][6]) / 6
    media_gm = (lista[3][1] + lista[3][2] + lista[3][3] + lista[3][4] + lista[3][5] + lista[3][6]) / 6
    media_wolkswagen = (lista[4][1] + lista[4][2] + lista[4][3] + lista[4][4] + lista[4][5] + lista[4][6]) / 6
    return media_fiat, media_ford, media_gm, media_wolkswagen 
    
def main(): 
    resultado_matriz = gerar_matriz(5, 3)
    ano_usuario = int(input("Digite o ano a ser consultado: "))
    maior_volume, ano_maior_volume = volume_maior(resultado_matriz)
    resultado_media_fiat, resultado_media_ford, resultado_media_gm, resultado_media_wolkswagen = volume_media(resultado_matriz)
    aux_posicao = aux_numero = 0
    for num_linha in range(len(resultado_matriz)):
        for num_coluna in resultado_matriz[num_linha]:
            if num_linha == 0:
                if num_coluna == ano_usuario:
                    indice_ano = resultado_matriz[num_linha].index(num_coluna, aux_posicao)
                else: aux_posicao += 1    
            else:
                if aux_numero == 0:
                    venda_maior = resultado_matriz[num_linha][indice_ano]
                    fabricante_venda = resultado_matriz[num_linha][0]
                    
                else:
                    if resultado_matriz[num_linha][indice_ano] > venda_maior:
                        venda_maior = resultado_matriz[num_linha][indice_ano]
                        fabricante_venda = resultado_matriz[num_linha][0]


    print(f'A fabricante que mais vendeu em {ano_usuario} foi a {fabricante_venda} com {venda_maior} mil unidades.')
    print(f'O ano de maior volume geral de vendas foi {ano_maior_volume} com {maior_volume} mil unidades.')
    print(f'A média anual de vendas de cada fabricante entre 2013 e 2018 foi:')
    print(f'A Fiat vendeu em média {resultado_media_fiat} unidades por ano.')
    print(f'A Ford vendeu em média {resultado_media_ford} unidades por ano.')
    print(f'A GM vendeu em média {resultado_media_gm} unidades por ano.')
    print(f'A Wolkswagen vendeu em média {resultado_media_wolkswagen} unidades por ano.')
if __name__ == '__main__':
    main()
