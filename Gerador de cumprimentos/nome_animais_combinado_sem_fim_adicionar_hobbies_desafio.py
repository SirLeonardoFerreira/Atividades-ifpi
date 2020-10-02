from random import*

#o programa continua em execução enquanto a variável for verdadeira 'True'
executa = True 

nomes_macho = ["Martin", "Jolir", "Ànubis", "oto patamar", "Scooby"]
nomes_femea = ["Mimosa", "Lola", "Penélope", "Gaia", "Amora"]

print("Serviço de escolha de nome para animais de estimação")
print("------------------")

quantidade = int(input("Quantos nomes você precisa?: "))
print('''
Menu
  c = obter nomes - para macho
  f = obter nomes - para fêmea
  a = adicionar nomes de animais macho
  b = adicionar nomes de animais fêmea
  d = remover nomes de animais macho
  e = remover nomes de animais fêmea
  p = imprimir nomes de animais macho
  s = imprimir nomes de animais fêmea
  q = sair
''')

while executa == True:
    menuChoice = input("\n>_").lower()
    # 'c' para um nome macho
    if menuChoice == 'c':
        for i in range(quantidade):
            #obtém um item aleatório da listas e adiciona-os ao nome
            print("você deve chamar seu animal de estimação de:" , choice(nomes_macho))
            print("De nada!")

    # 'f' para um nome fêmea
    elif menuChoice == 'f':
        for i in range(quantidade):
            #obtém um item aleatório da listas e adiciona-os ao nome
            print("você deve chamar seu animal de estimação de:" , choice(nomes_femea))
            print("De nada!")
            
    # 'a' para adicionar um nome de animal macho
    elif menuChoice == 'a':

        itemToAdd = input("Adicione o nome: ")
        if itemToAdd not in nomes_macho:
            nomes_macho.append(itemToAdd)
        else:
            print("O nome já está na lista!")
            
    # 'b' para adicionar um nome de animal fêmea
    elif menuChoice == 'b':

        itemToAdd = input("Adicione o nome: ")
        if itemToAdd not in nomes_femea:
            nomes_femea.append(itemToAdd)
        else:
            print("O nome já está na lista!")
            
    # 'd' para remover um nome de animal macho
    elif menuChoice == 'd':

        itemToDelete = input("Insira o nome a ser removido: ")
        #só remove um item se ele estiver na lista
        if itemToDelete in nomes_macho:
            nomes_macho.remove(itemToDelete)
        else:
            print("O nome não está na lista!")
    # 'e' para remover um nome de animal fêmea
    elif menuChoice == 'e':

        itemToDelete = input("Insira o nome a ser removido: ")
        #só remove um item se ele estiver na lista
        if itemToDelete in nomes_femea:
            nomes_femea.remove(itemToDelete)
        else:
            print("O nome não está na lista!")
            
    # 'p' para imprimir a lista de nomes de animais macho
    elif menuChoice == 'p':
        print(nomes_macho)
    
    # 's' para imprimir a lista de nomes de animais femea
    elif menuChoice == 's':
        print(nomes_femea)
        
    # 'q' para sair
    elif menuChoice == 'q':
        executa = False

    else:
        print("Escolha uma opção válida!")
