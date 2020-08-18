def maior_numero(a, b, c, d, e):
    numero_max = max(a, b, c, d, e)
    numero_min = min(a, b, c, d, e)
    media = (a + b + c + d + e) / 5
    return numero_max, numero_min, media

def main():
    numero_a = int(input())
    numero_b = int(input())
    numero_c = int(input())
    numero_d = int(input())
    numero_e = int(input())
    numero_max, numero_min, media = maior_numero(numero_a, numero_b, numero_c, numero_d, numero_e)
    print(f'{numero_max}')
    print(f'{numero_min}')
    print(f'{media:.2f}')

if __name__ == '__main__':
    main()
