def eh_primo(numero):
    num_composto = 0
    for intervalo in range(2, numero):
        if numero % intervalo == 0:
            num_composto += 1
    return num_composto
def main():
    numero_um = int(input())
    numero_dois = int(input())
    primo = 0
    for num in range(numero_um, numero_dois + 1):
        resultado_primo = eh_primo(num)
        if resultado_primo == 0 and num >= 2:
            primo = num
            print(f'{primo}')
if __name__ == '__main__':
    main()
