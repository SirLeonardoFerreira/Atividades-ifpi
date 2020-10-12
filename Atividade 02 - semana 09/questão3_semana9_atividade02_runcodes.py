from random import randint, seed
seed()
def gerar_matriz(linhas, colunas):
    matriz = []
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz

def media(num, qtd):
    return round((num / qtd), 4)

def main():
    numero_linhas = int(input())
    numero_colunas = int(input())
    resultado_matriz = gerar_matriz(numero_linhas, numero_colunas)
    soma_total_numeros = soma_primeira_linha = soma_ultima_coluna = aux_numero = qtd_numero = aux_posicao = 0
    for num_linha in range(len(resultado_matriz)):
        for num_coluna in resultado_matriz[num_linha]:
            soma_total_numeros += num_coluna
            qtd_numero += 1
            
            if num_linha == 0:
                soma_primeira_linha += num_coluna
                if aux_numero == 0:
                    num_maior = num_menor = num_coluna
                    aux_numero += 1
                    aux_posicao += 1
                elif aux_posicao == numero_colunas - 1:
                    soma_ultima_coluna += num_coluna
                    aux_posicao = 0
                    if num_coluna > num_maior:
                        num_maior = num_coluna
                    
                    elif num_coluna < num_menor:
                        num_menor = num_coluna
                        
                else:
                    if num_coluna > num_maior:
                        num_maior = num_coluna
                    
                    elif num_coluna < num_menor:
                        num_menor = num_coluna
                    aux_posicao += 1
                
            else:
                if aux_posicao == numero_colunas - 1:
                    soma_ultima_coluna += num_coluna
                    aux_posicao = 0
                    if num_coluna > num_maior:
                        num_maior = num_coluna
                    
                    elif num_coluna < num_menor:
                        num_menor = num_coluna
                    
                else:
                    
                    if num_coluna > num_maior:
                        num_maior = num_coluna
                    
                    elif num_coluna < num_menor:
                        num_menor = num_coluna
                    aux_posicao += 1
                            
    resultado_media = media(soma_total_numeros, qtd_numero)
    tupla = (soma_primeira_linha, soma_ultima_coluna, resultado_media, num_menor, num_maior)
    print(f'{tupla}')
if __name__ == '__main__':
    main()
    
