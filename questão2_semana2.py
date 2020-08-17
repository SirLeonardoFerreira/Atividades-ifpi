def caractere(a):
    return ord(a)

def main():
    caracte = input("Digite uma letra do seu teclado: ")
    caracte_x = caractere(caracte)
    print(f'O código númerico correspondente ao caractere ({caracte}) é o número ({caracte_x}).')

if __name__ == '__main__':
    main()
