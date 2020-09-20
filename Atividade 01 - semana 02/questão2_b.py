def media (a, b, c):
    return (a + b + c) / 3


def main():
    valor_a = int(input("Digite o valor de a: "))
    valor_b = int(input("Digite o valor de b: "))
    valor_c = int(input("Digite o valor de c: "))

    valor_media = media(valor_a, valor_b, valor_c)

    print(f"A média dos três valores é: {valor_media:.2f}")

if __name__ == '__main__':
    main()

