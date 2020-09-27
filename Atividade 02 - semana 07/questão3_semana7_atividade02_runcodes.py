def calculo_h(numero):
    for num in range(numero):
        if num == 0:
            H = 1

        else:
            H += (1 / (num + 1))
    return H
def main():
    numero = int(input())
    resultado_h = calculo_h(numero)
    print(f'{resultado_h:.4f}')

if __name__ == '__main__':
    main()
