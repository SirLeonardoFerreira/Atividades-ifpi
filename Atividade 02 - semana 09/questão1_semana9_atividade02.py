from random import randint, seed
seed()
def gerar_matriz(linhas, colunas):
    matriz = []
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(int(input("Digite mais um número: ")))
        matriz.append(linha)
    return matriz
def main():
    numero = int(input("Digite o número de linhas e colunas: "))
    resultado_matriz = gerar_matriz(numero, numero)
    aux_coluna = 0
    aux_numero = 0
    for num_linha in range(len(resultado_matriz)):
        for num_coluna in resultado_matriz[num_linha]:
            indice_coluna = resultado_matriz[num_linha].index(num_coluna, aux_coluna)
            if aux_numero == 0: 
                num_maior = num_menor = num_coluna 
                aux_coluna += 1
                aux_numero += 1
                tupla_maior_num = [num_linha, indice_coluna]
                tupla_menor_num = [num_linha, indice_coluna]
                
            else:
                if num_coluna > num_maior:
                    num_maior = num_coluna
                    tupla_maior_num = [num_linha, indice_coluna]
                elif num_coluna < num_menor:
                    num_menor = num_coluna
                    tupla_menor_num = [num_linha, indice_coluna]
                    
                aux_coluna += 0
            aux_coluna = 0
    
    print(f'O maior número está na posição {tuple(tupla_maior_num)}')
    print(f'O menor número está na posição {tuple(tupla_menor_num)}')
if __name__ == '__main__':
    main()
    
