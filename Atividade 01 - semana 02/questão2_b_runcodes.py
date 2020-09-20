def media (a, b, c):
    return (a + b + c) / 3


def main():
    valor_a = int(input())
    valor_b = int(input())
    valor_c = int(input())

    valor_media = media(valor_a, valor_b, valor_c)

    print(f"{valor_media:.2f}")

if __name__ == '__main__':
    main()

