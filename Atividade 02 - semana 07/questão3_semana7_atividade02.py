def calculo_h(numero):
    for num in range(numero):
        if num == 0:
            H = 1

        else:
            H += (1 / (num + 1))
    return H
def main():
    numero = int(input("Digite um número:" ))
    resultado_h = calculo_h(numero)
    print(f' O valor de H é {resultado_h:.4f}')

if __name__ == '__main__':
    main()
