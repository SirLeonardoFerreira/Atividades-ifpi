def maior_numero(a, b, c, d, e):
    return max(a, b, c, d, e)

def main():
    numero_a = int(input("Digite o primeiro número: "))
    numero_b = int(input("Digite o segundo número: "))
    numero_c = int(input("Digite o terceiro número: "))
    numero_d = int(input("Digite o quarto número: "))
    numero_e = int(input("Digite o quinto número: "))
    numero_max = maior_numero(numero_a, numero_b, numero_c, numero_d, numero_e)
    print(f'O maior número que foi digitado é {numero_max}.')

if __name__ == '__main__':
    main()
