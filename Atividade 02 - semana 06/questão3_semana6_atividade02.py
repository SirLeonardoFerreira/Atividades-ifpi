def main():
    while True:
        print("OPÇÕES: ")
        print("1 - SAUDAÇÃO")
        print("2 - BRONCA")
        print("3 - FELICITAÇÃO")
        print("0 - FIM")
        numero_opcao = int(input())
        if numero_opcao != 0:
            if  numero_opcao == 1:
                print("1 - Olá. Como vai?")

            elif  numero_opcao == 2:
                print("2 - Vamos estudar mais.")
    
            elif  numero_opcao == 3:
                print("3 - Meus Parabéns!")
            elif  numero_opcao > 3:
                print("Opção inválida.")

        if  numero_opcao == 0: break
    print("0 - Fim de serviço.")
if __name__ == '__main__':
    main()
    
