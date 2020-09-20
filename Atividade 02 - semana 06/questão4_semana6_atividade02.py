def main():
    soma = 0
    while True:
        print("CÓDIGO  PRODUTO         PREÇO (R$)")
        print("H       Hamburger       5,50")
        print("C       Cheeseburger    6,80")
        print("M       Misto Quente    4,50")
        print("A       Americano       7,00")
        print("Q       Queijo Prato    4,00")
        print("X       PARA TOTAL DA CONTA")
        codigo = input("Digite o código do item: ").upper()[0]
        if codigo != 'X':
            if codigo == 'H':
                soma += 5.50
                
            elif codigo == 'C':
                soma += 6.80
                
            elif codigo == 'M':
                soma += 4.50

            elif codigo == 'A':
                soma += 7.00

            elif codigo == 'Q':
                soma += 4.00

            elif not codigo in 'H C M A Q':
                print("Opção inválida.")

        if codigo == 'X': break

    if soma != 0:
        print(f'O total da conta é de R${soma:.2f}.')

if __name__ == '__main__':
    main()
