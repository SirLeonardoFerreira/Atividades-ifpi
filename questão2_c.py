def triplo (valor):
    return valor * 3


def main():
    valor_x = int(input("Digite o valor de x: "))
    valor_triplo = triplo(valor_x)
    print(f"O triplo é: {valor_triplo:.2f}")

if __name__ == '__main__':
    main()

