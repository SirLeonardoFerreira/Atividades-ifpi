def maior_numero(a, b, c, d, e):
    numero_max = max(a, b, c, d, e)
    numero_min = min(a, b, c, d, e)
    media = (a + b + c + d + e) / 5
    return numero_max, numero_min, media

def main():
    numero_a = int(input("Digite o primeiro número: "))
    numero_b = int(input("Digite o segundo número: "))
    numero_c = int(input("Digite o terceiro número: "))
    numero_d = int(input("Digite o quarto número: "))
    numero_e = int(input("Digite o quinto número: "))
    numero_max, numero_min, media = maior_numero(numero_a, numero_b, numero_c, numero_d, numero_e)
    print(f'O maior número que foi digitado é {numero_max}, o menor número que foi digitado é {numero_min} e a media é {media:.2f}')

if __name__ == '__main__':
    main()
