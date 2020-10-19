def converter(n):
    texto_novo = []
    for cod in range(len(n)):
        if not 'A' <= n[cod] <= 'Z':
            if n[cod] in 'ÁÀÂÃ':
                aux = 'A'
                texto_novo.append(aux)
            if n[cod] in 'Ç':
                aux = 'C'
                texto_novo.append(aux)
            if n[cod] in 'ÉÊ':
                aux = 'E'
                texto_novo.append(aux)
            if n[cod] in 'ÍÎ':
                aux = 'I'
                texto_novo.append(aux)
            if n[cod] in 'ÓÕÔ':
                aux = 'O'
                texto_novo.append(aux)
            if n[cod] in 'ÚÛ':
                aux = 'U'
                texto_novo.append(aux)
        else:
            texto_novo.append(n[cod])
    return texto_novo    
        
def main():
    texto = input().upper()
    texto_novo = converter(texto)
    qtd = {}
    for cod in range(len(texto_novo)):
        qtd[texto_novo[cod]] = texto_novo.count(texto_novo[cod])
    print(qtd)
        
if __name__ == '__main__':
    main()
