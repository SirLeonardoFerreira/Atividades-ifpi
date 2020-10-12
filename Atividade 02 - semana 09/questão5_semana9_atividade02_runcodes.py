def preenche_array(dim_0, dim_1, dim_2):
    dim_i = []
    for i in range(dim_0):
        dim_j = []
        for j in range(dim_1):
            dim_k = []
            for k in range(dim_2):
                dim_k.append(int(input()))
            dim_j.append(dim_k)
        dim_i.append(dim_j)
    return dim_i


def main():
    faturamento = preenche_array(4, 12, 3)
    MESES = ('Janeiro', 'Fevereiro', 'Março',
             'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro',
             'Outubro', 'Novembro', 'Dezembro')
    aux_filial = total_faturamento_primeira = total_faturamento_segunda = total_faturamento_terceira = total_periodo = 0
    ano = 2014
    i = 0
    for dim_um in range(len(faturamento)):
        for dim_dois in range(len(faturamento[dim_um])):
            for dim_tres in faturamento[dim_um][dim_dois]:
                if aux_filial == 0:
                    print(f'{ano};Filial 1;{MESES[i]};{dim_tres}')
                    total_faturamento_primeira += dim_tres
                    if MESES[i] == 'Dezembro':
                        print(f'TOTAL {ano} FILIAL 1;{total_faturamento_primeira}')
                    i += 1
                elif aux_filial == 1:
                    print(f'{ano};Filial 2;{MESES[i]};{dim_tres}')
                    total_faturamento_segunda += dim_tres
                    if MESES[i] == 'Dezembro':
                        print(f'TOTAL {ano} FILIAL 2;{total_faturamento_segunda}')
                    i += 1
                elif aux_filial == 2:
                    print(f'{ano};Filial 3;{MESES[i]};{dim_tres}')
                    total_faturamento_terceira += dim_tres
                    if MESES[i] == 'Dezembro':
                        print(f'TOTAL {ano} FILIAL 3;{total_faturamento_terceira}')
                    i += 1
                    
            if dim_dois == 3:
                aux_filial += 1
                i = 0
            
            elif dim_dois == 7:
                aux_filial += 1
                i = 0
                
        total_todas_filiais = total_faturamento_primeira + total_faturamento_segunda + total_faturamento_terceira
        print(f'TOTAL {ano} TODAS FILIAIS;{total_todas_filiais}')
        total_periodo += total_todas_filiais
        ano += 1
        aux_filial = i = total_faturamento_primeira = total_faturamento_segunda = total_faturamento_terceira = total_todas_filiais = 0
    print(f'TOTAL PERÍODO TODAS FILIAIS;{total_periodo}')
                

if __name__ == '__main__':
    main()
