from random import*

#o programa continua em execução enquanto a variável for verdadeira 'True'
executa = True 

adjetivos = ["maravilhoso", "acima da média", "excelente", "perfeito", "oto patamar"]

hobbies = ["andar de bicicleta", "programar", "fazer chá", "jogar bola"]

print("Gerador de Cumprimentos")
print("--------------------")

nome = input("Qual é o seu nome?: ")

print('''
Menu
  c = obter cumprimento
  a = adicionar hobby
  d = remover hobby
  p = imprimir hobbies
  q = sair
''')

while executa == True:
    menuChoice = input("\n>_").lower()

    # 'c' para um cumprimento
    if menuChoice == 'c':
        print("Aqui está o seu cumprimento", nome , ":")

        #obtém um item aleatório de ambas as listas e adiciona-os ao cumprimentos
        print(nome, "você é" , choice(adjetivos), "em" , choice(hobbies))
        print("De nada!")

    # 'a' para adicionar hobby
    elif menuChoice == 'a':

        itemToAdd = input("Adicione o hobby: ")
        hobbies.append(itemToAdd)

    # 'd' para remover um hobby
    elif menuChoice == 'd':

        itemToDelete = input("Insira o hobby a ser removido: ")
        #só remove um item se ele estiver na lista
        if itemToDelete in hobbies:
            hobbies.remove(itemToDelete)
        else:
            print("O hobby não está na lista!")
    # 'p' para imprimir a lista de hobbies
    elif menuChoice == 'p':
        print(hobbies)
        
    # 'q' para sair
    elif menuChoice == 'q':
        executa = False

    else:
        print("Escolha uma opção válida!")
