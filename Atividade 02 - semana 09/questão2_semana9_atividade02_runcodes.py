from random import randint, seed
seed()
def gerar_matriz(linhas, colunas):
    matriz = []
    temperatura_total = 0
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            temperatura = float(input())
            escala = input().upper()[0]
            if escala in 'C':
                temperatura = celsius_kelvin(temperatura)
            elif escala in 'F':
                temperatura = fahrenheit_kelvin(temperatura)
            temperatura_total += temperatura
            linha.append(
                (temperatura, escala)
            )
        matriz.append(linha)
    return matriz, temperatura_total

def celsius_kelvin(c):
    temperat = c + 273.15
    return round(temperat, 2)

def fahrenheit_kelvin(f):
    fah = ((f - 32) * 5 / 9) + 273.15
    return round(fah, 2)

def media_temperatura(t):
    return round(t / 12, 2)

def main():
    resultado_matriz, temp_total = gerar_matriz(12, 1)
    temperatura_media = media_temperatura(temp_total)
    print('TEMPERATURA MÉDIA ANUAL')
    print(f'{temperatura_media}K')
    print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    for num_linha in range(len(resultado_matriz)):
        for temp, _ in resultado_matriz[num_linha]:
            if temp > temperatura_media: 
                if num_linha == 0:
                    mes_aux = 'Janeiro'
                elif num_linha == 1:
                    mes_aux = 'Fevereiro'
                elif num_linha == 2:
                    mes_aux = 'Março'
                elif num_linha == 3:
                    mes_aux = 'Abril'
                elif num_linha == 4:
                    mes_aux = 'Maio'
                elif num_linha == 5:
                    mes_aux = 'Junho'
                elif num_linha == 6:
                    mes_aux = 'Julho'
                elif num_linha == 7:
                    mes_aux = 'Agosto'
                elif num_linha == 8:
                    mes_aux = 'Setembro'
                elif num_linha == 9:
                    mes_aux = 'Outubro'
                elif num_linha == 10:
                    mes_aux = 'Novembro'
                elif num_linha == 11:
                    mes_aux = 'Dezembro'
                print(f'{mes_aux}: {temp}K')
if __name__ == '__main__':
    main()
