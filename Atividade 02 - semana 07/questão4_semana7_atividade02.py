def eh_primo(numero):
    num_composto = 0
    for intervalo in range(2, numero):
        if numero % intervalo == 0:
            num_composto += 1
    return num_composto
def main():
    numero = int(input("Digite um número: "))
    resultado_primo = eh_primo(numero)
    if resultado_primo == 0 and numero >= 2:
        print(f'É um número primo.')
    else:
        print(f'Não é um número primo.')
if __name__ == '__main__':
    main()
