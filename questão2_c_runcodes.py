def triplo (valor):
    return valor ** 3


def main():
    valor_x = int(input())
    valor_triplo = triplo(valor_x)
    print(f"{valor_triplo:.2f}")

if __name__ == '__main__':
    main()

