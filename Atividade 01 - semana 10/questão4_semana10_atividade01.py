def main():
    dicionario_volgal = {}
    texto = input('Digite o texto: ')
    qtd_a = qtd_e = qtd_i = qtd_o = qtd_u = 0
    codigo_a = 'A'
    codigo_e = 'E'
    codigo_i = 'I'
    codigo_o = 'O'
    codigo_u = 'U'
    for qtd in range(len(texto)):
        if texto[qtd] in 'aAãÃâÂáÁ':
            qtd_a += 1
        elif texto[qtd] in 'eEéÉêÊ':
            qtd_e += 1
        elif texto[qtd] in 'iIíÍ':
            qtd_i += 1
        elif texto[qtd] in 'oOóÓ':
            qtd_o += 1
        elif texto[qtd] in 'uUúÚ':
            qtd_u += 1
            
    dicionario_volgal[codigo_a] = qtd_a
    dicionario_volgal[codigo_e] = qtd_e
    dicionario_volgal[codigo_i] = qtd_i
    dicionario_volgal[codigo_o] = qtd_o
    dicionario_volgal[codigo_u] = qtd_u

    for cod in dicionario_volgal:
        qtd_aux = dicionario_volgal[cod]
        print(f'{cod}: {qtd_aux}')
        
if __name__ == '__main__':
    main()
