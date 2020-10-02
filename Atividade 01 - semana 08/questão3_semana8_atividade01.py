def numeros_lidos(num):
    numeros_lidos = []
    for i in range(num):
        numero = float(input("Continue digitando números inteiros: "))
        numeros_lidos.insert(0, numero)
    return numeros_lidos

def media_notas(num):
    notas_lidas = []
    media = 0
    for i in range(num):
        notas_lidas.append(float(input("Digite as notas: ")))
    if len(notas_lidas) != 0:
        media = sum(notas_lidas) / len(notas_lidas)
    return notas_lidas, media

def letras(num):
    consoantes_lidas = []
    vogais_lidas = 0
    for i in range(num):
        letras_lidas = input("Digite um caractere: ")[0]
        if letras_lidas.upper() in 'AEIOU':
            vogais_lidas += 1
        else:
            consoantes_lidas.append(letras_lidas)
    return vogais_lidas, consoantes_lidas
def main():
    numero_lido = int(input("Digite um número inteiro: "))
    resultado_numeros_lidos = numeros_lidos(numero_lido)
    resultado_notas_lidas, resultado_media_notas = media_notas(numero_lido)
    resultado_vogais_lidas, resultado_consoantes_lidas = letras(numero_lido)
    print(f'{resultado_numeros_lidos}')
    print(f'{resultado_notas_lidas}')
    if numero_lido == 0:
        print(f'SEM NOTAS')
    else: print(f'{resultado_media_notas:.1f}')
    print(f'{resultado_vogais_lidas}')
    print(f'{resultado_consoantes_lidas}')
if __name__ == '__main__':
    main()
